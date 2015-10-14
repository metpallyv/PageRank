__author__ = 'Vardhaman'
import sys, string, math
from math import log
from math import modf
import operator
outlink_dict = {}
inlink_dict = {}
PRank = {}
new_PRank = {}
sinknodes = []
Pages = []
SortedPR = []

d = 0.85

#parse the file and create a inlink dictionary, list of sink nodes, outlink dictionary
#initial Page rank dictionary
def parse_file(inlink):
    #input = open('./inlink1.txt', 'r')
    input = open(inlink, 'r')
    for line in input.readlines():
        words = []
        words = string.split(line)
        inlink_dict[words[0]] = words[1:]
        Pages.append(words[0])

    len_dic = float(len(Pages))
    for page in Pages:
        PRank[page] = float(1) / len_dic

    for page in inlink_dict.keys():
        for q in inlink_dict[page]:
            if outlink_dict.has_key(q):
                outlink_dict[q] += 1
            else:
                outlink_dict[q] = 1

    for page in inlink_dict.keys():
        if not outlink_dict.has_key(page):
            sinknodes.append(page)
    #print (len(sinknodes))
    
#Page rank dump
def dump_pagerank():
    print("Dumping the page rank:")
    for page in PRank.keys():
       print ("Page Rank for the Page",page,"is",PRank.get(page))

#Perplexity calculation
def cal_Perplexity():
    hx = 0
    for page in PRank.keys():
        hx += PRank[page]*log(1/PRank[page],2)
    return 2**hx

#calculating page rank and checking for convergence at the same time
def cal_pagerank():
    i= 0
    perplexity = 0
    len_dic = float(len(inlink_dict.keys()))
    ite = 0
    #while not converged
    while(i <4):
        SinkPageRank = 0
        for page in sinknodes:
            SinkPageRank = float(SinkPageRank + PRank.get(page))
        for page in PRank.keys():
            new_PRank[page] = float(1 - d) / len_dic
            new_PRank[page] = new_PRank[page] + (d * float(SinkPageRank) / float(len_dic))
            for q in inlink_dict[page]:
                new_PRank[page] = new_PRank[page] + (d * float(PRank.get(q)) / float(outlink_dict.get(q)))
        for page in new_PRank.keys():
            PRank[page] = new_PRank.get(page)
        perplexity_new = cal_Perplexity()
        val1 = round(perplexity,3)
        val = round(perplexity_new,3)
        if val1 == val :
        	i = i+1
        else:
        	i = 0
        perplexity = perplexity_new
        print("Perplexity for iteration",ite,"is",perplexity_new)
	ite = ite+1

#retrieve top k documents
def top_rank():
    SortedPR = sorted(PRank.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(50):
        print (SortedPR[i])
inlink_rank = {}

#retreive top k inlink ranked pages
def top_inlink():
    #SortedInlink = sorted(inlink_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for page in inlink_dict.keys():
        inlink_rank[page] = len(inlink_dict.get(page))
    Inlink_rank = sorted(inlink_rank.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(50):
        print("Top inlink ranked pages are\n",Inlink_rank[i])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        inlink = sys.argv[1]
        parse_file(inlink)
        cal_pagerank()
        top_rank()
        top_inlink()
    else:
        print("Enter the inlink file for which page link should be calculated")
