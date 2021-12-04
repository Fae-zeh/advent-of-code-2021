# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:35:21 2021

@author: home
"""

import os
os.chdir(r"H:\advent of code 2021")

file = open('1.txt', 'r')
data = []
for line in file:
    data.append(int(line))
    
data_len = len(data)    
res = 0
for i in range(1, len(data)):
	if data[i] > data[i-1]:
		res += 1
print(res)