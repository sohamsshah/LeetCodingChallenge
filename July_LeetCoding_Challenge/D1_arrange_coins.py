# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:12:21 2020

@author: Soham Shah
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        if n <= 1:
            return n
        for i in range(0,n+1):
            ans = (i*(i+1))//2
            if ans > n:
                return i-1