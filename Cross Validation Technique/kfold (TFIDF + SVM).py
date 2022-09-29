# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:43:22 2021

@author: Zobi Tanoli
"""
from sklearn.metrics import confusion_matrix
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from textaugment import Wordnet
from textaugment import EDA
import math

#data = pd.read_csv('review_sentiments_dataset.csv')
data = pd.read_csv('review_sentiments_dataset.csv')
#print(data)

txt= data['Text']
#txt= txt.values.tolist()

#tt= data['Text']
#tt= tt.values.tolist()
#print(type(tt))
sent = data['Sentiment']
#sent= sent.values.tolist()



'''
txt=[]
t= Wordnet()
for i in tt:
    t1= t.augment(i)
    #print(t1)
    txt.append(t1)
len(txt)
#print(type(txt))
txt = pd.Series(txt)
#print(type(txt))
'''
allscor = []
kf =KFold(n_splits=40)

for train_index, test_index in kf.split(txt, sent):
   x_train, x_test = txt[train_index], txt[test_index]
   y_train, y_test = sent[train_index], sent[test_index]
   
   
   '''
   xtest=[]
   t= Wordnet()
   for i in x_test:
       t1= t.augment(i)
       #print(t1)
       xtest.append(t1)
   len(xtest)
   #print(type(txt))
   #x_test = pd.Series(xtest)
   #print(type(txt))
   Txttest=[]
   tRI= EDA()
   for i in xtest:
       tRI1= tRI.random_insertion(i)
       #print(tRI1)
       Txttest.append(tRI1)
   len(Txttest)
   x_test = pd.Series(Txttest)
   '''
   
   
   #print(type(x_test))

   tfidf = TfidfVectorizer()
   x_train = tfidf.fit_transform(x_train)
   x_test = tfidf.transform(x_test)

   clf = svm.SVC(kernel='linear', C = 2.0)
   clf.fit(x_train, y_train)
   y_pred = clf.predict(x_test)
   score = accuracy_score(y_test, y_pred)
   allscor.append(score)
   #print(classification_report(y_test, y_pred))
   #print(score)
   
   
   
#print(allscor)
'''
def Average(lst):
    return sum(lst) / len(lst)
  
# Driver Code

average = Average(allscor)

print('total average is:')
print(average)

variance = np.var(allscor)
print('total varience is:')
print(variance)

SD = np.std(allscor)
print('total standard Deviataion is:')
print(SD)

'''


