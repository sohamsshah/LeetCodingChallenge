# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:23:12 2020

@author: Soham Shah
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0:
            if amount == 0:
                return 1
            else:
                return 0
        
        mul = []
        for i in range(amount+1):
            mul.append(i)

        dp = [[0 for i in range(len(mul))] for j in range(len(coins))]

        for i in range(len(coins)):
            for j in range(len(mul)):
                if i == 0:
                    if j != 0:
                        if mul[j] % coins[i] == 0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    if coins[i] > mul[j]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]
        return dp[-1][-1]