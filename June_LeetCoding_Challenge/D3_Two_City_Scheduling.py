# -*- coding: utf-8 -*-
"""
@author: Soham Shah
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key = lambda x: x[0] -x[1])
        result = 0
        for i in range(len(costs)):
            if i< len(costs)/2:
                result += sorted_costs[i][0]
            else:
                result += sorted_costs[i][1]
        return result
<<<<<<< HEAD
    

        
    
        
=======
    

                
>>>>>>> Day 4
