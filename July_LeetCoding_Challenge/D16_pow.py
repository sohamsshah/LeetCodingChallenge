# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:33:05 2020

@author: Soham Shah
"""

def myPow(self, x, n):
    m = abs(n)
    ans = 1.0
    while m:
        if m & 1:
            ans *= x
        x *= x
        m >>= 1
    return ans if n >= 0 else 1 / ans

pow(4,5)

print(5&1)