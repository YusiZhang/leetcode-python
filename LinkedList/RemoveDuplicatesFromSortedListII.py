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
        pre, pre.next = self, head
        tmp = pre

        while head:
            if head.next and head.val == head.next.val:
                head = head.next            # skip same value elements, they should not in the list
                continue
            if tmp.next is head:
                tmp = tmp.next              # there is no skipping
            else:
                tmp.next = head.next        # there are some elements to skip
            head = head.next

        return pre.next