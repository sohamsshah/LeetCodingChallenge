# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:38:15 2020

@author: Soham Shah
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i,j in dic.items():
            if j==1:
                return i