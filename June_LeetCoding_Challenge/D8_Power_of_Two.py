# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:14:44 2020

@author: Soham Shah
"""

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        num = math.log(n,2)
        num = round(num, 10)
        if num.is_integer():
            return True
        else:
            return False
        
        