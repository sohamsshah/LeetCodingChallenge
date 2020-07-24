# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:14:49 2020

@author: Soham Shah
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt=0
        ans = str(bin(x^y))
        return (ans.count("1"))
        