# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:53:42 2020

@author: Soham Shah
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in range(len(graph)):
            dic[i] = graph[i]

        queue = [[0]]
        last = list(dic.keys())[-1]
        ans = []
        while len(queue) != 0:
            node = queue.pop(0)
            if node[-1] == last:
                ans.append(node)
            else:
                lis = dic[node[-1]]
                for i in lis:
                    queue.append(node + [i])
        return ans
