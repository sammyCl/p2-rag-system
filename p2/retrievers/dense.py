"""Dense retrieval: embed every chunk once, embed the query, and rank chunks by cosine similarity.

Ported from the 12 lab's retrieve.py (dense_rankings, the bge_instr arm): the chunks are encoded as
they are, and the query gets the instruction prefix that bge-small was trained with for retrieval.
The settings come from [dense] in p2.toml:

    model       the embedding model's Hugging Face name (default bge-small-en-v1.5)
    instruction the text put in front of every query ("" turns it off)

Every vector has length 1 (p2/embed.py), so the dot product of the query with a chunk is their cosine.
"""

from __future__ import annotations

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False

BGE_INSTRUCTION = "Represent this sentence for searching relevant passages: "


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        settings = cfg.table("dense")
        self.model = settings.get("model", embed.BGE)
        self.instruction = settings.get("instruction", BGE_INSTRUCTION)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        if not self.chunks:
            return np.zeros(0, dtype=np.float32)
        query = self.embedder.encode([self.instruction + text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
