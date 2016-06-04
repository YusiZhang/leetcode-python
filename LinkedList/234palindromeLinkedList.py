# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        new_head = None
        while slow:
            tmp = slow.next
            slow.next = new_head
            new_head = slow
            slow = tmp

        # compare the first and second half nodes
        while new_head: # while node and head:
            if new_head.val != head.val:
                return False
            new_head = new_head.next
            head = head.next
        return True