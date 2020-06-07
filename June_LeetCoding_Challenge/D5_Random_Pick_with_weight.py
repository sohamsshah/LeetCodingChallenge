# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:18:05 2020

@author: Soham Shah
"""

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        for weights in w:
            prefix_sum+= weights
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum
        

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        low,high = 0, len(self.prefix_sum)
        while low< high:
            mid = low+ (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid 
        return low
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
