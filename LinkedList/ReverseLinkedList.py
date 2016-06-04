# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head is not None:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        #!! head is current the next to new_head
        return new_head