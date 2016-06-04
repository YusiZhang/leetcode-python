"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        dummy = ListNode(0) # new starter of the sorted list
        dummy.next = head
        cur = head

        while cur.next:
            if cur.next.val >= cur.val: # 如果链表升序，cur指针一直向后移动, 直到一个节点的值小于前面节点的值，然后寻找插入的位置
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp

        return dummy.next


