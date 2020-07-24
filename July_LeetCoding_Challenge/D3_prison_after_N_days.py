# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:47 2020

@author: Soham Shah
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        arr = []
        for j in range(N):
            val = []
            for i in range(len(cells)):
                if i == 0 or i == len(cells) -1:
                    val.append(0)
                else:
                    if (cells[i-1] == 0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
                        val.append(1)
                    else:
                        val.append(0)
            if val not in arr:
                arr.append(val)
                cells = arr[-1].copy()
                val = []
            else:
                break
        if N>len(arr):
            return (arr[N%len(arr) - 1])
        else:
            return arr[N-1]