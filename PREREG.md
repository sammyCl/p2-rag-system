# Pre-registration (598E)

This file is for 598E students; it is the second half of the 598E rider, and 498E students can ignore it or delete it.

A pre-registration is a claim you write down, with the test that will judge it, before you can see the answer.
Its value is that the claim can be wrong in a way anyone can check, and that you cannot adjust it afterwards to fit the numbers.
A well-powered result that says "no effect as large as the one I cared about" scores as well as a confirmation, so you have no reason to bend the claim.

**Git history is how I will know the order.**
Commit this file, filled in through section 4, before the first commit that puts a judgment line into `eval/own/qrels.txt` (or any other file under `eval/own/`).
`uv run p2 check` reads `git log` to find the first commit in which sections 1 to 4 have no TODO marker left and some words of yours in each, and confirms that it comes before your first judgment; a copy that was filled in afterwards fails.
Right after that commit, `p2 check` names it and waits for your first judgment; it asks for section 5 separately, once you have scored your own corpus.
You may ingest your corpus and write queries first, but not the relevance judgments.
After that first commit, do not edit sections 1 to 4, because `p2 check` compares them with the commit where you filled them in.
If something must change, add a dated entry in section 6 and leave the original as it was.

You need your stage 1 scores for section 3, so score the shared corpus first.

---

## 1. Hypothesis

One sentence, about your own corpus, naming two of your systems and a direction.
For example: "On my corpus of Kubernetes documentation, `rerank` has a higher MRR@10 than `hybrid`, because the queries are paraphrases that a first-stage fusion ranks too low."
It should be something you could be wrong about.

For my corpus on Rocks and Minerals, I think that my rerank will have a higher nDCG@10 score than my hybrid. My corpus has a tendency to have documents reference each other or contain similar information, and I think this could interfere with the hybrid model as the bm25 may have difficulty identifying the main article, and the dense may be weaker with finding specific phrases. By having Claude rerank the predictions, I think it will be able to more accurately identify relevant articles.

---

## 2. The smallest effect that matters

Name one metric, MRR@10 or nDCG@10, and choose it now so you cannot pick the better one afterwards.
Then say how large a difference between the two systems would matter to a person using the search, and why that size.
A difference of 0.02 is usually not worth a reranker's cost in time and tokens.
In this course, choose a Δ of at least 0.15 unless you argue for a larger one, because a smaller gap takes more queries than one project can judge.
Call your number Δ (delta).

I am going to use nDCG@10 as my metric and a Δ of 0.2. I want to set my Δ higher than 0.15, because I want to make sure that switching to a rerank is worth the reranker's cost in time and tokens. For a user, having a difference of 0.2 could significantly change the articles that are used, such as the correct article going from being ranked third being reranked to first or the article going from missing to being included. These changes would mean the user is more likely to get the result they were looking for.

---

## 3. How many queries you need

The size of the gold set follows from three numbers: how large a difference you want to detect (Δ), how variable the per-query differences are (sd), and the usual choices of a 5% false-alarm rate and 80% power.

```
n = ((1.96 + 0.84) * sd / Δ)^2
```

Here sd is the standard deviation of the per-query differences between your two systems, which `results/results.json` holds for the shared practice queries.
Compute it from your stage 1 runs for the same two systems, or the nearest pair you have, and say which pair you used.
With only 20 practice queries the sd is itself noisy, so be generous and round up.

Some numbers to calibrate against.
At sd 0.3 and Δ 0.10 the formula gives about 71 queries, and with the t distribution's small-sample correction it is a few more, about 73.
At sd 0.3, a gold set of 30 queries can only detect a difference of about 0.15, which is why 30 queries cannot support a claim about a gap of 0.10.
The spreads you will measure on the shared practice queries are mostly larger than 0.3: from about 0.31 for `hybrid` against `bm25` to about 0.66 for `dense` against `bm25`.
For `rerank` against `hybrid` the sd is about 0.39, so a Δ of 0.10 needs about 120 queries, 0.15 about 55, and 0.20 about 31.
So the course's Δ of 0.15 means about 55 queries for that pair; at an sd of 0.66 it would mean about 150, so compare a pair whose spread you can afford.
Choose Δ and the size of your gold set together: the smallest effect that matters to a user, and a number of queries you can write and judge in the time you have.
If the two do not meet, say which one you gave ground on and why.

After you score the own corpus, the minimum detectable difference that `uv run p2 score` prints for your two systems is this same calculation run the other way.
It should come out at or below your Δ.
If it does not, your queries varied more than your stage 1 sd suggested, and you will say so in the outcome.

My sd is 0.255754, which is taken from the results/results.json for the comparison of rerank and hybrid for the nDCG@10 metric. 

```n = ((1.96 + 0.84) * sd / Δ)^2```
```n = ((1.96 + 0.84) * 0.255754 / 0.20)^2```
```n = 12.82```
```Rounded: n = 13```

Although my calculations say only 13 queries are required, I plan to do 30 queries as that is a requirement for my gold set.

---

## 4. The test, and what each result will mean

The test is the paired 95% interval of the mean difference between your two systems on your own gold set, from the `own-pairs` table that `uv run p2 score` writes in `EVAL.md`.
Write the rule now.
This is the default rule, and you can tighten it, but do not loosen it after you see your numbers.

| The interval is | I will say |
|---|---|
| entirely above zero in the direction I predicted | supported: the difference is distinguishable from zero |
| entirely on the other side of zero | contradicted: the opposite of my hypothesis holds on this gold set |
| around zero, with both ends inside plus or minus Δ | well-powered null: a difference as large as Δ is ruled out |
| around zero, with an end beyond plus or minus Δ | inconclusive: the gold set could not settle it, and I say so |

I will use this ruling. I am going to be comparing rerank minus hybrid, on nDCG@10, with Δ = 0.2.

---

## 5. Outcome (write this after the fact)

What was the interval?
Which row of the table in section 4 is it?
Did your gold set reach the size section 3 asked for, and what was the minimum detectable difference that `uv run p2 score` printed?
What would you do next, and what would you want a reader to take from this?

When comparing rerank and hybrid for the nDCG@10 metric, the final interval was [+0.035, +0.212], with a mean difference of +0.115, and a MDD of 0.127. This means that my result was in the following row of the table in Section 4:
```
| entirely above zero in the direction I predicted | supported: the difference is distinguishable from zero |
```
As a result, my claim is supported, but not 100% correct. The interval was entirely above zero in the direction I predicted, however I also stated that we would see a Δ of 0.2 for the nDCG@10 metric when comparing rerank and hybrid to justify using the rerank system. Since the interval was [+0.035, +0.212], the interval shows that the difference between hybrid and rerank is not consistent enough to justify the extra time and tokens that using Claude to rerank the relevant documents costs for my current gold-set.  

I reached an MDD of 0.127, since my Δ was 0.2, this means that my gold-set was large enough to identify the difference of Δ that I wanted. This is backed up by the math I did in Section 3 that showed 13 queries would be enough to show the difference, and my gold-set was 32 queries.

The two main changes I would make to my setup are both with my gold-set. After reviewing the metrics for my gold-set, specifically for the rerank system, I feel that my gold-set was too weak, as most of my systems scored unusually high for my corpus. I believe the main reason for this is that my queries were not broad enough and tended to focus on one topic or document. I also think that my relevance rule was too strict, as it reduced the number of relevant documents down to 1 for most of my queries. My next steps would be to write a new gold-set that had broader queries and multiple relevant documents. I also think I would write more queries to try and detect more differences between the different systems.

My current gold-set shows that my rerank system performed better than my hybrid system. This would likely translate to harder queries as well, because the rerank system would be able to rerank and identify documents that the hybrid system did not prioritize. As a result, I am inclined to say that with a stronger gold-set, my rerank system would likely have a more obvious difference when compared to the hybrid system.

---

## 6. Amendments

Dated entries only, one per change, each saying what changed and why.
Leave this section as it is if nothing changed.
