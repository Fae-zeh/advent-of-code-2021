# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:40:21 2021

@author: home
"""
import os
os.chdir(r"H:\advent of code 2021")

file = open('1.txt', 'r')
data = []
for line in file:
    data.append(int(line))

ans = 0    

def window(i):
    return data[i]+data[i+1]+data[i+2]

for i in range(0,len(data)-2):
    if window(i) > window(i-1):
        ans += 1
print(ans)
        
    