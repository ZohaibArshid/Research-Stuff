# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:34:58 2021

@author: Zobi Tanoli
"""
import pandas as pd
from deep_translator import MyMemoryTranslator
import time





data = pd.read_csv('review_sentiments_dataset.csv')
print(len(data))
txt = data['Text']
txt= txt.values.tolist()

French=[]


for t in txt:
    translated = MyMemoryTranslator(source="en", target="fr").translate(t)
    print(translated)
    French.append(translated)
    time.sleep(30)
print(French)