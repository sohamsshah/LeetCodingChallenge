# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:36:33 2020

@author: Soham Shah
"""

# Recursion

class Solution:
    
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value*10+root.val)
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val

 
# Iterative with Stack
                
class Solution:
    
    def sumNumbers(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res
        