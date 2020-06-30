# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:32:03 2020

@author: Soham Shah
"""

import collections

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1

if src == dst:
    print("0")

location =  collections.defaultdict(list)
prices = collections.defaultdict(lambda:float('inf'))

for u,v,p  in flights:
    location[u] +=[(v,p)]

q = [(src,-1,0)]
print(q)

while q:
    position,k,cost = q.pop(0)
    if position==dst or k == K:
        continue
    
    for neighbor,p in location[position]:
        if cost+p >= prices[neighbor]:
            continue
        else:
            prices[neighbor] = cost+p
            q +=[(neighbor, k+1, cost+p)]
    print(q)
    print(location)
    print(prices)
if prices[dst] < float('inf'):
    print(prices[dst])
else:
    print("-1")

    
