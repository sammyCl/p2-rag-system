"""Listwise reranking: Claude reorders a first-stage system's top 20, ported from the 13 lab's rerank_one().

For a query, the first stage (hybrid by default) ranks the documents, and its top 20 go to Claude
as numbered passages. Each passage is that document's best chunk under the first stage's chunk
ranking, with the document's title on top, so a long section shows the part that matched and not
only its opening lines (the lab cut every article to its first 600 characters).
The reply is forced into {"order": [20 numbers]}, each from 1 to 20; a reply that is not each number
once keeps the first-stage order. Documents below the 20 keep their first-stage order underneath.

The prompt is corpus-neutral, so the same system runs on the shared corpus and on your own: it says
nothing about mine regulations, and asks Claude to prefer a passage that states the answer over one
that only refers to another section.

search_chunks does the same over the first stage's top 20 chunks, for `p2 answer`.

The settings come from [rerank] in p2.toml:

    first       the first-stage system (default "hybrid")
    candidates  how many of its top results Claude reorders (default 20)
"""

from __future__ import annotations

from p2 import claude, retrievers

NEEDS_CLAUDE = True

PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
A passage that states the answer itself is more useful than one that only refers to another section or document without stating its content.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n):
    return {
        "type": "object",
        "properties": {
            "order": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": n},
                "minItems": n,
                "maxItems": n,
            }
        },
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        settings = cfg.table("rerank")
        self.first = retrievers.build(settings.get("first", "hybrid"), corpus, cfg)
        self.n = int(settings.get("candidates", 20))
        self.cfg = cfg
        self.model = cfg.model
        self.corpus = corpus
        self.chunks = {c.id: c for c in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)}

    def _passage(self, chunk_id):
        chunk = self.chunks[chunk_id]
        if chunk.n == 0:  # the first chunk already starts with the "# title" line
            return chunk.text.strip()
        return f"# {self.corpus.docs[chunk.docid].title}\n{chunk.text.strip()}"

    def _reorder(self, query, candidates, passage_ids):
        """candidates in Claude's order, or unchanged if the reply is not each number once."""
        if len(candidates) < 2:
            return candidates
        n = len(candidates)
        passages = "\n\n".join(f"[{i}] {self._passage(p)}" for i, p in enumerate(passage_ids, 1))
        reply = claude.call(
            PROMPT.format(n=n, query=query, passages=passages),
            schema(n),
            model=self.cfg.model,
            cache_dir=claude.cache_folder(self.cfg),
        )
        order = (reply.output or {}).get("order")
        if reply.error or not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            return candidates
        return [candidates[i - 1] for i in order]

    @staticmethod
    def _scored(ids, k):
        # Scores fall by 1 per rank, so they stay distinct and in order at six decimals.
        return [(i, float(len(ids) - r)) for r, i in enumerate(ids[:k])]

    def search(self, text, k):
        docs = [d for d, _ in self.first.search(text, len(self.corpus.docs))]
        best_chunk = {}
        for chunk_id, _ in self.first.search_chunks(text, len(self.chunks)):
            best_chunk.setdefault(chunk_id.rsplit("#", 1)[0], chunk_id)
        top = docs[: self.n]
        reordered = self._reorder(text, top, [best_chunk[d] for d in top])
        return self._scored(reordered + docs[self.n :], k)

    def search_chunks(self, text, k):
        ranked = [c for c, _ in self.first.search_chunks(text, max(k, self.n))]
        top = ranked[: self.n]
        reordered = self._reorder(text, top, top)
        return self._scored(reordered + ranked[self.n :], k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
