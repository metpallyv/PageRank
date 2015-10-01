# PageRank
The goal of this project is to implement PageRank on a collection of 183,811 web documents of size 2GB .

I implemented PageRank Algorithm based on the following :

1. Implement PageRank on the in-links(http://www.ccs.neu.edu/course/cs6200f14/wt2g_inlinks) file for the WT2g collection, a 2GB crawl of a subset of the web until the PageRank values converge . This in-links file is in the format: destination followed by a list of source documents. 
2.  Run your iterative version of PageRank algorithm until your PageRank values "converge". To test for convergence, calculate the perplexity of the PageRank distribution, where perplexity is simply 2 raised to the (Shannon) entropy of the PageRank distribution, i.e., 2H(PR). Perplexity is a measure of how "skewed" a distribution is --- the more "skewed" (i.e., less uniform) a distribution is, the lower its preplexity. Informally, you can think of perplexity as measuring the number of elements that have a "reasonably large" probability weight; technically, the perplexity of a distribution with entropy h is the number of elements n such that a uniform distribution over n elements would also have entropy h. (Hence, both distributions would be equally "unpredictable".) 
3.  Run your iterative PageRank algorthm, outputting the perplexity of your PageRank distibution until the change in perplexity is less than 1 for at least four iterations. 
4.  Sort the collection of web pages by the PageRank values you obtain and return the List the document IDs of the top 50 pages as sorted by PageRank, together with their PageRank values. Also, list the document IDs of the top 50 pages by in-link count, together with their in-link counts. 
5. Perform an analysis on top 10 pages sorted by page rank and in link counts using the Lemur web interface provided.
Usage of Lemur web interface to the collection by using the "e=docID" option with database "d=0", which is the index of the WT2g collection. For example, the link: 
http://fiji4.ccs.neu.edu/~zerg/lemurcgi_IRclass/lemur.cgi?d=0&e=WT04-B22-268 or
http://karachi.ccs.neu.edu/~zerg/lemurcgi_IRclass/lemur.cgi?d=0&e=WT04-B22-268
will bring up document WT04-B22-268, which is an article on the Comprehensive Test Ban Treaty.
6. Speculate why the top documents have high PageRank values, i.e., why is it that these particular pages are linked to by (possibly) many other pages with (possibly) high PageRank values. Are all of these documents ones that users would likely want to see in response to an appropriate query? Give some examples of ones that are and ones that are not. For those that are not "interesting" documents, why might they have high PageRank values? How do the pages with high PageRank compare to the pages with many in-links? In short, give an analysis of the PageRank results you obtain. 
