# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:32:27 2020

@author: Soham Shah
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        ans = []
        for i in s.most_common(n=k):
            ans.append(i[0])
        return ans