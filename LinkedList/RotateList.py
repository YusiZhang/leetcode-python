# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        1. head is none
        2. k is larger than list length
        """
        if not head:
            return head
        copyHead = head
        len = 1
        while copyHead.next:
            copyHead = copyHead.next
            len += 1
        copyHead.next = head # make it a cycle

        for i in range(len-k%len, 1, -1):
            head = head.next

        copyHead = head.next
        head.next = None

        return copyHead
