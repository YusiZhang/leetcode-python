"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        lastNode = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                #! not lastNode = l1
                lastNode.next = l1
                l1 = l1.next
            else:
                lastNode.next = l2
                l2 = l2.next
            lastNode = lastNode.next
        
        if l1 is not None:
            lastNode.next = l1
        if l2 is not None:
            lastNode.next = l2
            
        return dummy.next
            