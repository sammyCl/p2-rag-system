# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense: For the dense model, I chose to use the bge embedding model. I made this decision because I wanted to have a contextual model, because as seen in Lab 12, those tend to perform better. The main downside to this choice is that bge is more costly than potion, and can take more time. The dense model chunks 300 words together, with neighboring chunks sharing 50 words. 

Hybrid: For the hybrid model, I chose to use reciprocal rank fusion on the dense and bm25 models, as that fusion scored best during my Lab 13 experimentation. I tried to perform some hyperparameter tuning for my hybrid model by experimenting with different k values, however when I tried committing a k value of 20 to my Git, the CI check failed. As a result, I reverted back to k=60.

Rerank: The reranker saw the hybrid's top 20 different candidates and utilized the Sonnet model.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.588 | 0.534 | 0.493 |
| hybrid | 0.600 | 0.469 | 0.455 |
| rerank | 0.725 | 0.800 | 0.742 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.250 | 0.643 | 0.917 |
| dense | MRR@10 | 0.286 | 0.657 | 0.681 |
| dense | nDCG@10 | 0.222 | 0.601 | 0.682 |
| hybrid | Recall@10 | 0.571 | 0.357 | 0.917 |
| hybrid | MRR@10 | 0.518 | 0.143 | 0.792 |
| hybrid | nDCG@10 | 0.444 | 0.188 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.500 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.714 | 0.550 | 1.000 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.037 | [-0.317, +0.250] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.027 | [-0.245, +0.301] | 0.396 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.025 | [-0.287, +0.241] | 0.381 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.025 | [-0.225, +0.200] | 0.313 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.038 | [-0.180, +0.081] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.063 | [-0.218, +0.079] | 0.218 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.013 | [-0.167, +0.200] | 0.273 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.065 | [-0.279, +0.131] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.038 | [-0.217, +0.127] | 0.251 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.100 | [-0.117, +0.308] | 0.317 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.224 | [+0.007, +0.429] | 0.306 | rerank higher |
| rerank minus dense | Recall@10 | +0.138 | [-0.025, +0.317] | 0.249 | not distinguishable |
| rerank minus dense | MRR@10 | +0.266 | [+0.115, +0.432] | 0.232 | rerank higher |
| rerank minus dense | nDCG@10 | +0.250 | [+0.089, +0.417] | 0.238 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.125 | [+0.042, +0.233] | 0.143 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.331 | [+0.163, +0.506] | 0.249 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.287 | [+0.178, +0.400] | 0.160 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

The differences that are distinguishable from 0 occur when the rerank values are higher. This occurs when we do rerank minus bm25 for MRR@10 and nDCG@10, rerank minus dense for MRR@10 and nDCG@10, and all values for rerank minus hybrid. Everything else is considered to not be distinguishable.

The minimal detectable difference at 20 queries is between 0.143 (rerank minus hybrid recall@10) and 0.415 (dense minus bm25 recall@10). The minimal detectable difference says that for any gap smaller than that value, we would not be able to reliably detect it. 

Lecture 12 argued that no search method is the best at every type of question. This claim is supported by the scores per query class, which shows that bm25 performed the best for identifier questions and dense performed the best for paraphrased questions. However, their scores for the others were very lacking.

Lecture 13 argued that using an LLM as a reranker can significantly improve the ranking. This is reflected in some of our data tables, which demonstrate the reranker clearly performing better than any other model for MRR@10 and nDCG@10. Lecture 13 also argued that fusion helps when one partner is weak but can hurt when a partner is already strong. However, our MDD numbers show indistinguishable differences at this time.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I used rerank to answer the 12 questions because it had the best overall performance, which can be seen in most instances in the scores per system, scores per class, and the comparison table, for the MRR@10 and nDCG@10 metrics.

I did not change prompts/answer.txt.

Cited answers audit:
```
a02: Makes 2 claims. 
    Claim 1: Supported, almost exact quote.
    Claim 2: Supported, reworded quote.
Overall Citation: Logical match, the text specifically focuses on the incombustible content of rock dust. However, the quote that says the incombustible content of the combined dust must not be less than 80% does not explicitly state this is for an area with no methane. This can be assumed because the following sentence does say that values change if methane is present.
Verdict: Matches

a04: Makes 2 claims.
    Claim 1: Supported, reworded quote. 
    Claim 2: Supported, reworded quote.
Overall Citation: Logical match, the text explicitly covers when the underground evacuation drills shall occur and how they will be held. However, it does not directly state whether this is for metal, nonmetal, or both types of mines.
Verdict: Assumption made, but seems to match.

a07: Makes 3 claims.
    Claim 1: Supported, direct quote.
    Claim 2: Supported, direct quote.
    Claim 3: Supported, some wording left out of claim.
Overall Citations: Logical match, the text explicitly covers when berms are required and what their setup should be. However, it does not directly state whether this is for metal, nonmetal, or both types of mines.
Verdict: Assumption made, but seems to match.
```
---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My corpus is 260 Wikipedia articles about rocks (155 rock types) and minerals (105 minerals). Each rock/mineral has its own document, with the references section removed. It is around 2.0MB on disk. As my documents are from Wikipedia, they are covered under the cc-by-sa-4.0 license.

There were a couple documents that I did not end up keeping because they were not long enough. I set a 100 word cutoff for my documents, so a couple ended up getting dropped. This makes it so I am a little less confident in the documents I decided to keep with only 100 words, such as comendite.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

I have a total of 32 queries, with 12 hand written and 20 written by Claude. I used the identifier (7), paraphrase (13), and mixed (12) classes to have questions so each method could excel at one (bm25->identifier, dense->paraphrase, etc).

A document will be considered relevant if it has a clear answer to the query. This means that the document must be about the query's subject, or have direct quotes that answer the query. It must either have a clear definition of a term (identifier), a clear connection to the query (not a brief cross-reference) (paraphrase/mixed), or must have a quote that can be used to/reworded to answer the question (paraphrase/mixed). If multiple documents fit this requirement, all documents are considered to be relevant. If the document simply cross-references or tangentially covers a topic, it will not be considered relevant.

To find candidates, I had Claude pool the articles for each query. It ran bm25 (top 10 articles), dense (top 10 articles), and hybrid (top 20 articles to match rerank) on my queries. Claude also performed a keyword search over the corpus. I then either evaluated the title of each article to be irrelevant, or read each article and decided whether or not it was relevant for the query. I also performed a consistency pass with Claude's help, where I had it look over what I marked to be relevant and then see if my reasoning was consistent. I then did my own verification to make sure everything still aligned.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.930 | 0.875 | 0.868 |
| dense | 0.802 | 0.731 | 0.730 |
| hybrid | 0.953 | 0.862 | 0.869 |
| rerank | 0.992 | 1.000 | 0.985 |
| ablation/dense_potion | 0.812 | 0.755 | 0.751 |

32 judged queries; nDCG uses binary labels; a random ranking of the 260 documents would get recall@10 near 0.038.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=13) | mixed (n=12) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.857 | 0.904 | 1.000 |
| bm25 | MRR@10 | 0.786 | 0.846 | 0.958 |
| bm25 | nDCG@10 | 0.804 | 0.808 | 0.969 |
| dense | Recall@10 | 0.857 | 0.590 | 1.000 |
| dense | MRR@10 | 0.729 | 0.522 | 0.958 |
| dense | nDCG@10 | 0.756 | 0.496 | 0.969 |
| hybrid | Recall@10 | 1.000 | 0.885 | 1.000 |
| hybrid | MRR@10 | 0.857 | 0.738 | 1.000 |
| hybrid | nDCG@10 | 0.895 | 0.735 | 1.000 |
| rerank | Recall@10 | 1.000 | 0.981 | 1.000 |
| rerank | MRR@10 | 1.000 | 1.000 | 1.000 |
| rerank | nDCG@10 | 1.000 | 0.962 | 1.000 |
| ablation/dense_potion | Recall@10 | 0.714 | 0.731 | 0.958 |
| ablation/dense_potion | MRR@10 | 0.643 | 0.590 | 1.000 |
| ablation/dense_potion | nDCG@10 | 0.662 | 0.599 | 0.968 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=12) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.979 | 0.900 | +0.079 | [-0.042, +0.229] | not distinguishable |
| bm25 | MRR@10 | 1.000 | 0.800 | +0.200 | [+0.075, +0.350] | hand higher |
| bm25 | nDCG@10 | 0.969 | 0.806 | +0.163 | [+0.025, +0.320] | hand higher |
| dense | Recall@10 | 0.875 | 0.758 | +0.117 | [-0.133, +0.350] | not distinguishable |
| dense | MRR@10 | 0.802 | 0.688 | +0.114 | [-0.175, +0.386] | not distinguishable |
| dense | nDCG@10 | 0.789 | 0.695 | +0.094 | [-0.169, +0.346] | not distinguishable |
| hybrid | Recall@10 | 0.958 | 0.950 | +0.008 | [-0.125, +0.150] | not distinguishable |
| hybrid | MRR@10 | 0.938 | 0.817 | +0.120 | [-0.072, +0.309] | not distinguishable |
| hybrid | nDCG@10 | 0.916 | 0.841 | +0.075 | [-0.089, +0.242] | not distinguishable |
| rerank | Recall@10 | 0.979 | 1.000 | -0.021 | [-0.062, +0.000] | not distinguishable |
| rerank | MRR@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| rerank | nDCG@10 | 0.979 | 0.988 | -0.009 | [-0.058, +0.024] | not distinguishable |
| ablation/dense_potion | Recall@10 | 0.875 | 0.775 | +0.100 | [-0.150, +0.342] | not distinguishable |
| ablation/dense_potion | MRR@10 | 0.875 | 0.683 | +0.192 | [-0.058, +0.433] | not distinguishable |
| ablation/dense_potion | nDCG@10 | 0.847 | 0.693 | +0.153 | [-0.093, +0.390] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.142 | +0.104 | +0.037 | [-0.258, +0.312] | not distinguishable |
| MRR@10 | +0.112 | +0.198 | -0.086 | [-0.375, +0.183] | not distinguishable |
| nDCG@10 | +0.111 | +0.180 | -0.069 | [-0.339, +0.185] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.95 (12 queries), claude 0.80 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 12 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.128 | [-0.292, +0.034] | 0.234 | not distinguishable |
| dense minus bm25 | MRR@10 | -0.144 | [-0.288, -0.009] | 0.205 | bm25 higher |
| dense minus bm25 | nDCG@10 | -0.137 | [-0.278, -0.007] | 0.198 | bm25 higher |
| hybrid minus bm25 | Recall@10 | +0.023 | [-0.078, +0.125] | 0.155 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.013 | [-0.114, +0.077] | 0.140 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | +0.002 | [-0.096, +0.087] | 0.134 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.151 | [+0.047, +0.276] | 0.169 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.131 | [+0.037, +0.242] | 0.147 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.139 | [+0.049, +0.242] | 0.140 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.062 | [+0.000, +0.156] | 0.122 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.125 | [+0.031, +0.234] | 0.141 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.117 | [+0.039, +0.215] | 0.130 | rerank higher |
| rerank minus dense | Recall@10 | +0.190 | [+0.073, +0.326] | 0.184 | rerank higher |
| rerank minus dense | MRR@10 | +0.269 | [+0.132, +0.417] | 0.208 | rerank higher |
| rerank minus dense | nDCG@10 | +0.254 | [+0.128, +0.391] | 0.192 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.039 | [+0.000, +0.109] | 0.090 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.138 | [+0.042, +0.249] | 0.150 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.115 | [+0.035, +0.212] | 0.127 | rerank higher |
| ablation/dense_potion minus bm25 | Recall@10 | -0.117 | [-0.258, +0.016] | 0.196 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.120 | [-0.234, -0.016] | 0.159 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.117 | [-0.233, -0.012] | 0.161 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | +0.010 | [-0.125, +0.141] | 0.191 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | +0.024 | [-0.063, +0.122] | 0.136 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | +0.021 | [-0.070, +0.122] | 0.140 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.141 | [-0.266, -0.031] | 0.169 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.107 | [-0.204, -0.025] | 0.131 | hybrid higher |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.118 | [-0.217, -0.035] | 0.132 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.180 | [-0.312, -0.062] | 0.184 | rerank higher |
| ablation/dense_potion minus rerank | MRR@10 | -0.245 | [-0.380, -0.115] | 0.193 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.234 | [-0.364, -0.113] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."

Hypothesis: I switched from bge to potion for my ablation's dense model. I believe that this will lower my MRR@10 because the model will no longer take the context of different words into consideration.

The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_potion minus bm25 | Recall@10 | -0.117 | [-0.258, +0.016] | 0.196 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.120 | [-0.234, -0.016] | 0.159 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.117 | [-0.233, -0.012] | 0.161 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | +0.010 | [-0.125, +0.141] | 0.191 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | +0.024 | [-0.063, +0.122] | 0.136 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | +0.021 | [-0.070, +0.122] | 0.140 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.141 | [-0.266, -0.031] | 0.169 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.107 | [-0.204, -0.025] | 0.131 | hybrid higher |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.118 | [-0.217, -0.035] | 0.132 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.180 | [-0.312, -0.062] | 0.184 | rerank higher |
| ablation/dense_potion minus rerank | MRR@10 | -0.245 | [-0.380, -0.115] | 0.193 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.234 | [-0.364, -0.113] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_potion against dense (BASE = "dense" in p2/retrievers/dense_potion.py): it helped 4 queries, hurt 5 and left 23 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_potion RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| o18 | paraphrase | claude | 0.000 | 1.000 | +1.000 | helped |
| o05 | mixed | hand | 0.500 | 1.000 | +0.500 | helped |
| o07 | paraphrase | hand | 0.000 | 0.500 | +0.500 | helped |
| o15 | paraphrase | claude | 0.167 | 0.500 | +0.333 | helped |
| o17 | paraphrase | claude | 1.000 | 0.333 | -0.667 | hurt |
| o31 | identifier | claude | 1.000 | 0.500 | -0.500 | hurt |
| o22 | paraphrase | claude | 0.500 | 0.333 | -0.167 | hurt |
| o04 | paraphrase | hand | 0.125 | 0.000 | -0.125 | hurt |
| o30 | identifier | claude | 0.100 | 0.000 | -0.100 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

For my ablation, I chose to approach my dense model in a new way and switched from bge to potion. My prediction was that this switch would lower my dense model's MRR@10 value. Based on the comparison after running them:
```
| ablation/dense_potion minus dense | MRR@10 | +0.024 | [-0.063, +0.122] | 0.136 | not distinguishable |
```
It appears that the potion model performed slightly better, but not well enough to be considered a stronger model. My gold set is only reliably detecting a difference between the two models when there is an MRR@10 gap of 0.136 or higher. My gap was 0.024 is too small for the test to tell them apart. Therefore, my hypothesis is inconclusive. I also believe that if I used more queries, a distinctive difference may become clear.

The switch from bge to potion for the dense model improved the results of 4 queries, hurt the results of 5 queries, and left 23 queries unchanged. The top changes are as follows:

o18, o05, o07, and o15 all improved. After reviewing what those queries were I realized that they tended to be questions where I struggled with determining the relevant documents. I had to make several hard decisions when classifying relevant documents because some documents were adjacent to answering the questions, but missed some of the key information that I was looking for. I think that the bge dense model likely included documents I ultimately deemed to be irrelevant because it took more context into account, while I chose not to include them.

o17, o31, o22, o04, and o30 all regressed. After reviewing those questions, it looks like they were all identifier or paraphrase questions. This makes me think that potion struggled more with them because it did not reference the context for the keywords or struggled to identify the correct keywords.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 217,674 | 4,455 | 81.8 | 18,140 | 371 | 6.8 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 251,983 | 4,436 | 87.5 | 20,999 | 370 | 7.3 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 269,151 | 4,434 | 93.9 | 22,429 | 370 | 7.8 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 262,218 | 4,519 | 98.9 | 21,852 | 377 | 8.2 |
| traces/own-own-rerank.jsonl | rerank | 32 | 32 | 2 | 556,785 | 2,912 | 131.5 | 17,400 | 91 | 4.1 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 0 | 249,517 | 1,966 | 58.2 | 12,476 | 98 | 2.9 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 270,853 | 1,820 | 64.3 | 13,543 | 91 | 3.2 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 261,705 | 1,902 | 64.3 | 13,085 | 95 | 3.2 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 279,991 | 1,820 | 66.7 | 14,000 | 91 | 3.3 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 1 | 525,239 | 4,071 | 116.0 | 13,131 | 102 | 2.9 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 12,476 | 2.9 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.266 | [-0.432, -0.115] | 12,476 | 2.9 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.331 | [-0.506, -0.163] | 12,476 | 2.9 | rerank higher |
| own: bm25 minus rerank | 32 | -0.125 | [-0.234, -0.031] | 17,400 | 4.1 | rerank higher |
| own: dense minus rerank | 32 | -0.269 | [-0.417, -0.132] | 17,400 | 4.1 | rerank higher |
| own: hybrid minus rerank | 32 | -0.138 | [-0.249, -0.042] | 17,400 | 4.1 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_potion.jsonl | dense_potion | 32 | 0.04 | 1.2 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 32 | 0.02 | 0.8 |
| traces/retrieval/own-own-dense.jsonl | dense | 32 | 0.25 | 7.7 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 32 | 0.28 | 8.9 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.06 | 2.9 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.31 | 15.4 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.36 | 18.1 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.12 | 3.1 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.50 | 12.6 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.68 | 17.1 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.725 | 0.800 | 0.738 |
| rerank.r2 | 0.725 | 0.800 | 0.742 |
| rerank.r3 | 0.725 | 0.800 | 0.738 |
| range (max minus min) | 0.000 | 0.000 | 0.004 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.125 | [+0.042, +0.233] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.125 | [+0.042, +0.233] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.125 | [+0.042, +0.233] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.331 | [+0.163, +0.506] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.331 | [+0.163, +0.506] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.331 | [+0.163, +0.506] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.283 | [+0.175, +0.396] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.287 | [+0.178, +0.400] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.283 | [+0.175, +0.396] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
