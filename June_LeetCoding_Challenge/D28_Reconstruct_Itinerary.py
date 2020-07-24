# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:11:57 2020

@author: Soham Shah
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for i in tickets:
            if i[0] not in adj:
                adj[i[0]] = [i[1]]
            else:
                adj[i[0]].append(i[1])
        for i in adj:
            adj[i].sort()
            
        result = []
        def dfs(s):
            while s in adj and len(adj[s]) > 0:
               
                v = adj[s].pop(0)
               
                dfs(v)
            result.append(s)

        

        dfs("JFK")
        return result[::-1]