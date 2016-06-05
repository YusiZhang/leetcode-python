# coding=utf-8
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n or head is None:
            return head

        pre, pre.next = self, head
        head = pre

        for i in xrange(1, m):
            if head is None:
                return None
            head = head.next

        premNode = head
        mNode = head.next
        nNode = mNode
        postnNode = nNode.next

        for i in xrange(m, n):
            if postnNode is None:
                return None
            tmp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = tmp
        mNode.next = postnNode
        premNode.next = nNode

        return pre.next
