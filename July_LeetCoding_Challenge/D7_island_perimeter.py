# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:19:16 2020

@author: Soham Shah
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if i != 0 and i != len(grid) -1:
                        if grid[i+1][j] == 1:
                            cnt+=1
                        if grid[i-1][j] == 1:
                            cnt+=1
                    else:
                        if i == 0 and i != len(grid) -1 :
                            if grid[i+1][j] == 1:
                                cnt+=1
                        elif i == len(grid) -1 and i != 0:
                            if grid[i-1][j] == 1:
                                cnt+=1
                    if j != 0 and j != len(grid[0]) -1:
                        if grid[i][j+1] == 1:
                            cnt+=1
                        if grid[i][j-1] == 1:
                            cnt+=1
                    else:
                        if j == 0 and j != len(grid[0]) - 1:
                            if grid[i][j+1] == 1:
                                cnt+=1
                        elif j != 0 and j == len(grid[0]) - 1:
                            if grid[i][j-1] == 1:
                                cnt+=1

                else:
                    if i == 0:
                        cnt+=1
                    if i == len(grid) -1:
                        cnt+=1
                    if j == 0:
                        cnt+=1
                    if j ==  len(grid[0]) - 1:
                        cnt+=1
        return cnt



                    
                    
                    