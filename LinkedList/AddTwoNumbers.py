# coding=utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 注意两个链表长度可能不一致
        # 注意可能其中一个链表为空
        head = ListNode(0)
        pointer = head
        carry = 0
        while True:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            pointer.val = carry % 10
            carry /= 10
            # 运算未结束，新建一个节点用于存储答案，否则退出循环
            if l1 is not None or l2 is not None or carry != 0:
                pointer.next = ListNode(0)
                pointer = pointer.next
            else:
                break

        return head
