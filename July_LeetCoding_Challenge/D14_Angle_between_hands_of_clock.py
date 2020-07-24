# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:30:52 2020

@author: Soham Shah
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12: 
            hour=0
        long_hand = hour + minutes/60
        short_hand = (12*minutes)/60
        diff = abs(long_hand - short_hand)
        return min(diff*30, 360 - (diff*30))