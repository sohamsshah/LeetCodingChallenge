# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:13:44 2020

@author: Soham Shah
"""

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
