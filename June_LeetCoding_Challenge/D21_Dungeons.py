# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:05:04 2020

@author: Soham Shah
"""

class Solution:
    def calculateMinimumHP(self, dungeons: List[List[int]]) -> int:
    
        dp = [[0 for i in range(len(dungeons[0]))] for j in range(len(dungeons))]
        dp[-1][-1] = max(1, 1 - dungeons[-1][-1])

        for i in range(len(dungeons)-1, len(dungeons)):
            for j in range(len(dungeons[0])-2,-1,-1):
                dp[i][j] = max(dp[i][j+1] - dungeons[i][j],1)

        for i in range(len(dungeons)-2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1] - dungeons[i][-1],1)


        for i in range(len(dungeons)-2, -1, -1):
            for j in range(len(dungeons[0])-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - (dungeons[i][j]))

        return (dp[0][0])