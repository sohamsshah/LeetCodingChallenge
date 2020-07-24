# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:29:09 2020

@author: Soham Shah
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            if n&1 > 0: result+=1
            n >>=1
        return result
        