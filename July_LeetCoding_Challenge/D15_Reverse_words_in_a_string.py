# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:31:20 2020

@author: Soham Shah
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        lis = []
        store = ""
        for i in s:
            if i!=" ":
                store+=i
            if i== " ":
                lis.append(store)
                store =""
        lis.append(store)
        print(lis)
        store = ""
        
        for i in lis[::-1]:
            if i!="":
                store+=(i+" ")
        return store[:-1]