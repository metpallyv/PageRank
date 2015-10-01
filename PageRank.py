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

#checking for convergence
def check_for_convergence(perp_list):
    frac1,val1 = modf(perp_list[0])
    frac2, val2 = modf(perp_list[1])
    frac3, val3 = modf(perp_list[2])
    frac4, val4 = modf(perp_list[3])
    if ((val1 == val2) and (val2 == val3) and (val3 == val4)):
        return True
    else:
        return False

#calculating page rank
def cal_pagerank():
    ite= 0
    len_dic = float(len(inlink_dict.keys()))
    perp_list = []
    perplexity = cal_Perplexity()
    perp_list.append(perplexity)
    print("Perplexity for iteration",ite,"is",perplexity)
    ite = ite +1
    while(ite <=3):
        SinkPageRank = 0
        for page in sinknodes:
            SinkPageRank = SinkPageRank + PRank.get(page)
        for page in inlink_dict.keys():
            new_PRank[page] = float(1.0 - d) / len_dic
            new_PRank[page] = new_PRank[page] + float(d * SinkPageRank) / len_dic
            for q in inlink_dict[page]:
                new_PRank[page] = new_PRank[page] + float(d * PRank.get(q)) / outlink_dict.get(q)
        for page in new_PRank.keys():
            PRank[page] = new_PRank.get(page)
        perplexity = cal_Perplexity()
        perp_list.append(perplexity)
        print("Perplexity for iteration",ite,"is",perplexity)
        ite = ite+1
    #check_for_convergence
    while(not check_for_convergence(perp_list)):
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
        perplexity = cal_Perplexity()
        print("Perplexity for iteration",ite,"is",perplexity)
        ite = ite +1
        temp = []
        temp = perp_list[1:]
        temp.append(perplexity)
        perp_list = temp
        #dump_pagerank()

#retrieve top k ranks documents
def top_rank():
    SortedPR = sorted(PRank.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(50):
        print (SortedPR[i])
inlink_rank = {}

#retreive top k inlink ranked pages
def top_inkink():
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
        top_inkink()
    else:
        print("Enter the inlink file for which page link should be calculated")
