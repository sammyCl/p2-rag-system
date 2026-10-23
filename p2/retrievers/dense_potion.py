"""Ablation of dense: potion-retrieval-32M in place of bge-small, with no query instruction.

The one change is the embedding model. potion was not trained with bge's instruction prefix, so the
query goes in as it is. Everything else is dense's: the same chunks, cosine ranking, and k.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer
from p2.retrievers.dense import Dense

NEEDS_CLAUDE = False

BASE = "dense"


class DensePotion(Dense):
    def __init__(self, corpus, cfg):
        ChunkScorer.__init__(self, corpus, cfg)
        self.model = embed.POTION
        self.instruction = ""
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)


def build(corpus, cfg):
    return DensePotion(corpus, cfg)
