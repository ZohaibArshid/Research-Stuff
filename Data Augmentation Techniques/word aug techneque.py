# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:33:16 2021

@author: Zobi Tanoli
"""
import csv
import pandas as pd
import nlpaug.augmenter.word as naw


data = pd.read_csv('review_sentiments_dataset.csv')
#print(data)

txt= data['Text']
txt= txt.values.tolist()
          
          
          
          
aug = naw.ContextualWordEmbsAug()
augmented_data = aug.augment(txt)



with open("itrator.csv", "w", newline= "", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in augmented_data:
        writer.writerow([row])