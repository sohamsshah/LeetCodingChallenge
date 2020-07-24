# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:30:48 2020

@author: Soham Shah
"""

nums = [1,2]
nums.sort()
dp = [1 for i in range(len(nums))]
maxi = 1
for i in range(1, len(nums)):
    for j in range(i-1, -1, -1):
        if nums[i]%nums[j] == 0:
            if dp[j]>=maxi:
                dp[i]+=(dp[j])
                maxi = max(maxi, dp[i])
                break

prev = -1
ans = []

while True:
    if maxi==0:
        break
    for i in dp:
        if i == maxi:
            ans.append(i)
            dp.remove(i)
            break
    maxi-=1


        

   