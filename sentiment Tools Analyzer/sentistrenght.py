# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:10:12 2021

@author: Zobi Tanoli
"""

from sentistrength import PySentiStr
import pandas as pd
#from sklearn import preprocessing
#le = preprocessing.LabelEncoder()
#from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import string
import re
import pandas as pd
import csv


data = pd.read_csv('review_sentiments_dataset.csv')
#print(data)

txt = data['Text']
#txt= txt.values.tolist()
print(txt)
#txt = np.array(txt).ravel()


'''
txt = [float(x.strip()) for x in txt] 
print(type(txt))
print(txt)
'''


senti= PySentiStr()
senti.setSentiStrengthPath('C:/Users/Zobi Tanoli/Anaconda3/Lib/site-packages/sentistrength/SentiStrength.jar')
senti.setSentiStrengthLanguageFolderPath('C:/Users/Zobi Tanoli/Anaconda3/Lib/site-packages/sentistrength/SentStrength_Data_Sept2011/')
#print(senti.getSentiment('test'))



#print(senti.getSentiment('Such an easy app to use, really quick and easy to set up and had absolutely no problems with drivers.'))
#print(senti.getSentiment('All rides have been enjoyable.'))
#txtfloat= pd.to_numeric(text, errors='coerce')
#print(txtfloat)

sent=[]

for t in txt:
    X= senti.getSentiment(t)
    sent.append(X)
print(len(X))
print(sent)

lst = [val for sublist in sent for val in sublist]
print(lst)
#print(type(lst))
#len(lst)

list_string =list(map(str, lst)) 
#print(list_string)




for i,value in enumerate(list_string):
    list_string[i] = value.replace('5' , 'positive').replace('4' , 'positive').replace('3' , 'positive').replace('2' , 'positive').replace('1' , 'positive')
    print(list_string)
    
for i,value in enumerate(list_string):
    list_string[i] = value.replace('0' , 'neutral')
    
for i,value in enumerate(list_string):
    list_string[i] = value.replace('-positive' , 'negative')
  
    
print(len(list_string))


with open("data.csv", "w", newline= "") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in list_string:
    #for i in range(len(senti6)):
        writer.writerow([row])















'''
text=[]
for s in txt:
    map(float,re.split('['+'|'.join(string.punctuation)+']',s))
    text.append(s)
print(text)



def attempt_float(txt):
    try:
        return float(txt)
    except:
        return txt


#  sent= float (['i am a boy'])



senti = PySentiStr()

#for sent in txt:
result = senti.getSentiment('i am a boy')
print(result)


'''




































'''
for s in text:
    str_arr=float(s)
    print(type(str_arr))



# OR, if you want dual scoring (a score each for positive rating and negative rating)
result = senti.getSentiment(str_arr, score='dual')
print(result)


# OR, if you want binary scoring (1 for positive sentence, -1 for negative sentence)
result = senti.getSentiment(str_arr, score='binary')
print(result)


# OR, if you want trinary scoring (a score each for positive rating, negative rating and neutral rating)
result = senti.getSentiment(str_arr, score='trinary')
print(result)

'''

