"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            # push each head to the min heap
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(None)
        curr = head
        while heap:
            # pop the min node and insert it to the result list
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            # push a new head after the inserted head to the min heap
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))

        return head.next
