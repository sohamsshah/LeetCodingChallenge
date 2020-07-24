# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:33:14 2020

@author: Soham Shah
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            while len(a) != len(b):
                b = "0" + b
        elif len(a) < len(b):
            while len(a) != len(b):
                a = "0" + a
        cin = 0
        ans = ""
        for i,j in zip(a[::-1], b[::-1]):
            val = int(i) ^ int(j) ^ cin
            ans = str(val) + ans
            cin = int(i) & int(j) | cin & (int(i)^int(j))    
        if cin == 0:
            return ans
        else:
            return str(cin) + ans