# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:02:57 2020

@author: Soham Shah
"""

class Solution:
    
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if val == root.val or root is None:
            return root
                
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right,val)
        
                
            
        