# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:05:04 2020

@author: Soham Shah
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxh, lc = 0, len(citations)
        for i, n in enumerate(citations):
            print(i,n)
            maxh = max(min(lc-i, n), maxh)
        return (maxh)
