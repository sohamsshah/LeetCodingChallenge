# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:34:02 2020

@author: Soham Shah
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # arr = []
        # while head != None:
        #     print(head)
        #     if head.next.val == val and head.next != None:
        #         head.next = head.next.next
        #     arr.append()
        #     head = head.next
        # print(head)   
        # return ans
    
        dummy_head = ListNode(-1)
        dummy_head.next = head   
        current_node = dummy_head
        while current_node.next != None:
            print(current_node)
            print(dummy_head)
            print("\n")
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next