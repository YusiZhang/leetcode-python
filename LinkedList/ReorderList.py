# coding=utf-8
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return
        # find middle
        prev = ListNode(None)
        slow = fast = head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev_slow.next = None
        head2 = None
        while slow:
            tmp = slow.next
            slow.next = head2
            head2 = slow
            slow = tmp

        # reconstruct lisk
        p1 = head
        p2 = head2
        while p1:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2  # this will cover the last element of p2 is appended to p1.
            # p1: 1->2 p2: 5->4->3. "3" will be appended after 4: 1->5->2->4->3
            if tmp1 is None:
                break
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2

