"""Hybrid retrieval: reciprocal rank fusion (RRF) of two systems, ported from the 13 lab's rrf().

Each system ranks every document (or every chunk, for search_chunks), and a document scores the
sum of 1 / (k + rank) over the rankings it appears in. RRF uses only ranks, so the two systems'
scores never need to be on the same scale (bm25's run into the tens, dense's are cosines below 1).

One change from the lab: a document that bm25 scores 0 shares no word with the query, and its rank
is only document id order (padding), so it is left out of bm25's ranking and gets nothing from it.
It can still score through dense. The same holds for any system whose score is 0 or below.

The settings come from [hybrid] in p2.toml:

    systems  the two systems to fuse (default ["bm25", "dense"])
    rrf_k    the constant k in 1 / (k + rank) (default 60, the lab's)
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

DROP_ZERO = {"bm25"}  # systems whose score of 0 means "no match", not a real rank


class Hybrid:
    def __init__(self, corpus, cfg):
        settings = cfg.table("hybrid")
        self.names = list(settings.get("systems", ["bm25", "dense"]))
        self.rrf_k = float(settings.get("rrf_k", 60))
        self.systems = [retrievers.build(name, corpus, cfg) for name in self.names]
        self.n_docs = len(corpus.docs)

    def _ranking(self, name, pairs):
        if name in DROP_ZERO:
            pairs = [(i, s) for i, s in pairs if s > 0]
        return [i for i, _ in pairs]

    def _fuse(self, rankings, k):
        scores: dict[str, float] = {}
        for ranking in rankings:
            for rank, item in enumerate(ranking, 1):
                scores[item] = scores.get(item, 0.0) + 1 / (self.rrf_k + rank)
        return order(scores.items())[:k]

    def search(self, text, k):
        rankings = [self._ranking(n, s.search(text, self.n_docs)) for n, s in zip(self.names, self.systems)]
        return self._fuse(rankings, k)

    def search_chunks(self, text, k):
        rankings = [self._ranking(n, s.search_chunks(text, len(s.chunks))) for n, s in zip(self.names, self.systems)]
        return self._fuse(rankings, k)


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
