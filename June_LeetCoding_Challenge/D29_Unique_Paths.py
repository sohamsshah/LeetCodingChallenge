# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:07:45 2020

@author: Soham Shah
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for i in range(n)]

        for i in range(len(dp)):
            if i==0:
                dp[i] = [1 for i in range(m)]
            dp[i][0] = 1 

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]