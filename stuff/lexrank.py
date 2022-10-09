#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:17:25 2017

@author: iiestcst
"""

from nltk import *
import re
import urllib2
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from collections import namedtuple
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import operator
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Digraph

 
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def remove_stopword(text):
    cachedStopWords = stopwords.words("english")
    text = ' '.join([word for word in text.split() if word not in cachedStopWords])
    return text
 
def textrank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)
    
    #sentence index tagging
    sentence_mod=[]
    processed_sent=[]
    index=0
    for item in sentences:
      
        new_item=remove_stopword(item)
      
        index=index+1
        item += u' '
        item +=str(index)
        sentence_mod.append(item)
        
        new_item +=u' '
        new_item +=str(index)
        processed_sent.append(new_item)

        
    
    #print processed_sent

 
    bow_matrix = CountVectorizer().fit_transform(processed_sent)
    
   
    
    normalized = TfidfTransformer().fit_transform(bow_matrix)
    
    #print normalized
 
    similarity_graph = normalized * normalized.T
 
    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    #nx.draw(nx_graph)
    #plt.show()
    return sorted(((scores[i],s) for i,s in enumerate(processed_sent)),
                  reverse=True),sentence_mod
    
def get_only_text(url):
#"""
#return the title and the text of the article
#at the specified url
#"""
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

#
feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'))
to_summarize = map(lambda p: p.text, feed.find_all('guid'))
target=open("result.txt","w")
for article_url in to_summarize[:1]:
    headline,title = get_only_text(article_url)
#    print '_____________________________'
#    print headline
#    print '‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐'   
#    target.write(title.encode('utf-8'))
#t=open('/home/iiestcst/AnacondaProjects/Code/14_aug (backup)/input.txt', 'r')
#title=t.read()
#print "*****************************************************************************"
#print title[0].replace(u'Share this with Email Facebook Messenger Messenger Twitter Pinterest WhatsApp LinkedIn Copy this link These are external links and will open in a new window','')
  
#print title
txt_rnk,sentence_mod=textrank(title)

print ("******************************************")
#print txt_rnk
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
length = len(txt_rnk)
n=int(length*0.25)
#print "n:------------------->",n
i=0
result=[]
while i< n:
    #print str(txt_rnk[i][1]).replace(u'Share this with Email Facebook Messenger Messenger Twitter Pinterest WhatsApp LinkedIn Copy this link These are external links and will open in a new window','')
    #print txt_rnk[i][1]
    result.append(txt_rnk[i][1])   
    i=i+1





    
result.sort(key = lambda x: int(x.rsplit(' ',1)[1]))# sort according sentence index #

result_sent=''
result_index=[]
for item in result:
    for k in sentence_mod:
        if item.rsplit(None, 1)[-1]==k.rsplit(None, 1)[-1]:
            result_sent+=k.rsplit(' ', 1)[0] #remove sentence index from the result #
            result_index.append(k.rsplit(' ', 1)[1])
print (str(result_sent.encode('utf8')).replace('Share this with Email Facebook Messenger Messenger Twitter Pinterest WhatsApp LinkedIn Copy this link These are external links and will open in a new window',''))

#print "____________________________"
#print result_index
#print "____________________________+++++++++++"
#print str(title.encode('utf8')).replace('Share this with Email Facebook Messenger Messenger Twitter Pinterest WhatsApp LinkedIn Copy this link These are external links and will open in a new window','')