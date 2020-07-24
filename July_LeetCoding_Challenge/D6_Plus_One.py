# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:15:08 2020

@author: Soham Shah
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = ""
        for i in digits:
            ans = ans + str(i)
        ans = int(ans)
        ans = ans + 1
        return list(str(ans))