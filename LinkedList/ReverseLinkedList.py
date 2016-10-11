# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # new_head = None
        # while head is not None:
        #     tmp = head.next
        #     head.next = new_head
        #     new_head = head
        #     head = tmp
        # #!! head is current the next to new_head
        # return new_head
        # prev = None
        # count = 1
        # while head:
        #     # print "head.next: " + str(head.a
        #     # head.next, head, prev = prev, head.next, head
        #     print count
        #     head, prev, head.next = head.next, head, prev
        #     count += 1

        # return prev
        prev = None
        
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    # head = node1
    newHead = Solution().reverseList(node1)

    while newHead:
        print str(newHead.val) + "->"
        newHead = newHead.next
