# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:56:48 2021

@author: Zobi Tanoli
"""

import pandas as pd
import csv
from textaugment import Wordnet
from textaugment import EDA
import nltk
import string
#nltk.download('averaged_perceptron_tagger')

data = pd.read_csv('review_sentiments_dataset.csv')
print(data)

txt = data['Text']
len(txt)


# --------- Synonym-------
tt=[]
t= Wordnet()
for i in txt:
    t1= t.augment(i)
    print(t1)
    tt.append(t1)
len(tt)

#----------Random Insertion----
RI=[]
tRI= EDA()
for i in txt:
    tRI1= tRI.random_insertion(i)
    print(tRI1)
    RI.append(tRI1)
len(RI)


# ------------Random Deletion------

RD=[]
tRI= EDA()
for i in txt:
    tRd1= tRI.random_deletion(i)
    print(tRd1)
    RD.append(tRd1)
len(RD)

# ------------Random Swap-----

RS=[]
tRS= EDA()
for i in txt:
    tRS1= tRS.random_swap(i)
    print(tRS1)
    RS.append(tRS1)
len(RS)






with open("itrator.csv", "w", newline= "", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in RS:
        writer.writerow([row])
