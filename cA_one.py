#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:34:43 2018

@author: aananya
"""
import csv
rows = list( csv.reader(open('interview_scent.csv')) )

#QUESTION 1-a:
rc = 0
for row in rows:
# do something
    if row[4] != 'None':
        rc += 1
    
print rc
#ans- 22377-1 = 22376

#QUESTION 1-b:
lst = []
for row in rows:
    if row[4] != 'None':
        lst.append(row[4])

ul = set(lst)
length = len(ul)-1
print length


#ans- 542-1 = 541

#QUESTION 1-c:
#22376 are divided into 541 diff unique labels
#eg- lst.count("green tea") 
      #so- lst.count(a[i]) 
     # e is from 0 to 542
     
for e in ul:
    print lst.count(e)
    print e

