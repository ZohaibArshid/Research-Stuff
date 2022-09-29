# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:36:53 2021

@author: Zobi Tanoli
"""
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from numpy import mean
from numpy import std
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv('Augsynonym.csv')
print(data)



txt= data['Text']
#txt= txt.values.tolist()
print(txt)
sent = data['Sentiment']
#sent= sent.values.tolist()






kf =KFold(n_splits=5)
model = LogisticRegression(solver= 'liblinear')
vectorizer = CountVectorizer()

acc_score = []
Xtrain=[]
xtest=[]


for train_set, test_set in kf.split(txt):
    print(train_set, len(train_set))
    print(test_set, len(test_set))
    X_train , X_test = txt.iloc[train_set],txt.iloc[test_set]
    y_train , y_test = sent[train_set] , sent[test_set]
    #print(type(X_train))
    Xtrain.append(X_train)
    xtest.append(X_test)

'''
for x in Xtrain:
    str.lower(x)

for y in xtest:
    str.lower(x)
'''

xtrain = vectorizer.fit_transform(Xtrain)
testx = vectorizer.fit_transform(xtest)
    
model.fit(xtrain,y_train)
pred_values = model.predict(testx)
     
acc = accuracy_score(pred_values , y_test)
acc_score.append(acc)

'''
Etype=[]
Etype.append(txt)
Etype.append(sent)


scaler = MinMaxScaler(feature_range=(0, 1))
txt = scaler.fit_transform(txt)
'''

#scores = cross_val_score(model, txt, sent, scoring='accuracy', cv=kf)
#print('Accuracy: %.3f(%.3f)'% (mean(scores), std(scores)))

'''

def simple_split(Etype,y, length, split_mark=0.7):
    if split_mark > 0. and split_mark < 1.0:
        n= int(split_mark*length)
    else:
        n= int(split_mark)
    X_train = Etype[:n].copy()
    print( X_train)
    X_test = Etype[n:].copy()
    print( X_test)
    y_train = y[:n].copy()
    #print( y_train)
    y_test = y[n:].copy()
    #print( y_test)
    return X_train,X_test,y_train,y_test

vectorizer = CountVectorizer()
X_train,X_test,y_train,y_test= simple_split(Etype[0],Etype[1],len(Etype[0]))
print(len(X_train),len(X_test),len(y_train),len(y_test))
#txt.shape()


X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

linear = svm.SVC(kernel='linear', gamma='auto', C=2).fit(X_train, y_train)



y_pred = linear.predict(X_test)
'''


'''

i=1
kf =KFold(n_splits=5)
for train_set, test_set in kf.split(X=X):
    print(train_set, len(train_set))
    print(test_set, len(test_set))
    i += 1


le =LabelEncoder()
data['Text'] = le.fit_transform(data['Text'])
#data['Sentiment'] = le.fit_transform(data['Sentiment'])
print(data)

X_train, X_test, y_train, y_test = train_test_split(txt, sent , test_size= 0.3)

X_train= X_train.reshape(-1, 1)
y_train= y_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
    
model =svm.SVC(kernel='linear', gamma='auto', C=2).fit(X_train, y_train)
'''
    
    
    
