# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I did not realize that I had to answer this prompt before running my score, I thought I only had to do PREREG first, so I have already seen my score. I apologize for doing these in the wrong order.

I can say that I expected rerank to perform best since it performed the best in lab 13 and against the shared corpus. This is reflected in my hypothesis for prereg as well, because I predicted that the rerank would perform better than the hybrid. I expected dense or bm25 to perform the worst because they focus on either keywords or applying context, not both. I leaned towards bm25 performing worse because it performs the best on identifier questions, and I knew those would make up a much smaller portion of the queries.

In terms of my corpus, I chose to do one on Rocks and Minerals. I have an interest in geophysics and geology, and actually minored in geophysical engineering here at Mines. As a result, I knew that I wanted to do something in this realm. I chose to have my corpus about rocks and minerals because I knew that it would be straightforward to get to the necessary document and token requirement. 

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

There were a couple forks in the road that I encountered, one was what embedding model I chose. I chose to use the bge embedding model, because during Lab 12 it performed more consistently than the potion model, since it took into account the context of the document. This choice did cost time, as the bge model takes longer to run since it takes more context into account.

Here is what I observed for Lab 12: 

| Class | potion R@5 | potion MRR | bge R@5 | bge MRR |
|---|---|---|---|---|
| all | 0.78 | 0.76 | 0.78 | 0.73 |
| identifier | 0.89 | 0.85 | 1.00 | 0.80 |
| paraphrase | 0.67 | 0.42 | 0.50 | 0.53 |
| mixed | 0.78 | 1.00 | 0.83 | 0.87 |

Additionally, my choice of corpus put me down a specific path. My choice of a rocks and minerals corpus has resulted in my documents having a decent amount of overlap, as different rocks and minerals reference each other, and have similar methods of formation, uses, etc. While I stand by my choice, since it helps to answer questions I am interested in, there are costs that come with having such overlap, such as systems misidentifying documents.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

The main area where I overruled the agent was when I was identifying relevant documents. I would classify the documents, and then use Claude to make sure I was applying my rules consistently. This helped to identify areas where I was lacking, but also helped me to strengthen my relevance rule and confidently categorize the different documents, as there were many suggestions that I disagreed with. Claude would bring up documents that seemed to fit the query, and I was able to explain why I disagreed regarding its relevance. This was how I was able to establish my strong relevance rule.

For example, when I was figuring out the relevant documents for o29, Claude repeatedly suggested including a document that discussed how a mineral helped to understand the atmosphere in the past, despite the query being about what banded iron formations tell us about Earth's early oceans. Each time, I would disagree and point out that the question was specifically asking about how banded iron formations related to information about Earth's early oceans, not the atmosphere. I would also make sure I did not add it to the relevant documents for the query.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

I do not trust the score metrics for my reranker on my corpus, as they are above 95%. This would mean that my reranker would have to be nearly perfect, which does not make sense given its performance on the shared corpus. Since my other systems improved dramatically on my corpus compared to the shared corpus, I believe that my scores appear higher than they should because my gold-set is weak. My queries had significantly more keywords included in them than the shared gold-set did, and my relevance rule was strict enough that for most queries I only had one relevant document. This combination likely made it straightforward for my systems to identify the documents, as they could primarily rely on keywords.

The main test I did was looking at how much the shared gold-set focused on keywords compared to my gold-set, and I saw the following:

Content-word overlap by query class:
| Query class | Shared (n) | Own (n) |
| --- | ---: | ---: |
| identifier | 0.95 (7) | 1.00 (7) |
| paraphrase | 0.11 (7) | 0.83 (13) |
| mixed | 0.51 (6) | 0.80 (12) |
| all | 0.53 (20) | 0.86 (32) |

This demonstrated to me that my queries were likely too keyword-reliant. 

In order to trust these metrics, I would have to see almost the same values on a harder gold-set that relied less on keywords. This plan is described further in Section 5.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

I want to improve my gold-set. I would like to go back through and make more difficult queries that have fewer keywords, are more vague, and have multiple relevant documents attached to them. The queries will also be broader so I can justify having multiple relevant documents for each query. I will also want to make my relevance rule a little more forgiving so I can include relevant documents that contain the answer to a query, but may not have the answer as their focus or most important detail.

To check whether my gold-set has improved, I would want to run my systems against my corpus and updated gold-set. If my scores are more similar to the ones of the shared corpus, I can safely say that my gold-set improved. If my scores remain about the same, it is possible that my corpus is easier for the systems to utilize than the shared corpus. Either way, I will be able to conclude whether my oddly high metrics are due to a weak gold-set, or a compatible corpus.

To see the current metrics, the easiest place would be to look at Section 4 of `EVAL.md`. To see the current queries and relevance documents, you would want to look at queries.tsv and qrels.txt under the directory for my corpus.
