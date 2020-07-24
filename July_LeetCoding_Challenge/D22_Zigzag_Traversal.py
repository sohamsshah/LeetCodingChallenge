# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:14:24 2020

@author: Soham Shah
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: 
            return
        queue = [[root]]
        ans = [[root.val]]
        while queue != [[]]:
            lis = queue.pop(0)
            queue.append([])
            ans.append([])
            for x in lis:
                if x.right != None:
                    queue[0].append(x.right)
                    ans[-1].append(x.right.val)
                if x.left != None:
                    queue[0].append(x.left)
                    ans[-1].append(x.left.val)
        ans.pop()
        for i in range(len(ans)):
            if i%2 == 0:
                ans[i].reverse()
        return ans