"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        # dummy.next points to where head originally is
        dummy.next = head
        head = dummy
        
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next
        
