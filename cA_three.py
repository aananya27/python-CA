#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 22:04:33 2018

@author: aananya
"""
import re

text1 = 'Carlisle Farm Specialist F-1 Farm Tire - 12.5L-15 LRF/12 ply (Wheel Not Included) '
m = re.search('\d\d\.\d\w-\d\d \w\w\w/\d\d', text1)
if m:
    found = m.group(0)   
print found

text2 = 'Evergreen EU72 205/50ZR16 OWL87W RT-5 Truck tire'
m = re.search('\d\d\d\/\d\d\w\w\d\d \w\w\w\d\d\w', text2)
if m:
    found = m.group(0)
print found

text3 = 'Goodyear Marathon Trailer Tire w/Galvanized Rim ST215/75R14 LRC (5 Lug On 4.5)'
m = re.search('\w\w\d\d\/\d\d\w\d\d', text3)
if m:
    found = m.group(0)
print found

text4 = '1 X New Achilles \"ATR Sport\" 265/35ZR18 97W XL High Performance Tires 265/35/18'
m = re.search('\d\d\d\/\d\d\w\w\d\d \d\d\w \w\w', text4)
if m:
    found = m.group(0)
print found

text5 = 'Set of 2 ZEEMAX Heavy Duty All Steel ST235/85R16-14PR TL Trailer Tire - 11073'
m = re.search('\w\w\d\d\d\/\d\d\w\d\d-\d\d\w\w \w\w', text5)
if m:
    found = m.group(0)
print found

text6 = '1 X New Lexani LXHT-106 LT285/70R17/8 118Q BW All Season Performance SUV Tires'
m = re.search('\w\w\d\d\d\/\d\d\w\d\d\/\d \d\d\d\w \w\w', text6)
if m:
    found = m.group(0)
print found

text7 = '1 X New Nankang N889 Mudstar M/T LT245/75R16 120/116N E/10 Ply ROWL Mud Tires MT '
m = re.search('\w\w\d\d\d\/\d\d\w\d\d \d\d\d\/\d\d\d\w \w\/\d', text7)
if m:
    found = m.group(0)
print found

text8 = 'Pirelli Night Dragon Motorcycle Front Tire 130/90-16 2211500'
m = re.search('d\d\d\/\d\d-\d\d', text8)
if m:
    found = m.group(0)
print found
