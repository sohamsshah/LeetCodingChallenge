# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:10:36 2020

@author: Soham Shah
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return 
        
        root.left,root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root