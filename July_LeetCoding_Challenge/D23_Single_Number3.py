# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:24:07 2020

@author: Soham Shah
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                ans.append(i)
        return (list(set(nums).difference(set(ans))))