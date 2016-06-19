import heapq
from collections import deque
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str
        result = ""
        maxHeap = []
        m = {}
        for s in str:
            m[s] = m.get(s, 0) + 1
        for key,value in m.items():
            heapq.heappush(maxHeap, (-1*value,key))

        waitQueue = deque()

        while len(maxHeap) > 0:
            current = heapq.heappop(maxHeap)
            result += current[1]
            # current[0] -= 1 tuple is immutable, cannot assign value
            new_current = (-1 * current[0] - 1, current[1])
            waitQueue.append(new_current)

            if len(waitQueue) < k:
                continue
            front = waitQueue.popleft()
            if front[0] > 0:
                heapq.heappush(maxHeap, (-1*front[0], front[1]))

        return result if len(result) == len(str) else ""


        # This solution is for exact K char apart. Not for at least K char apart.
        # if k == 0:
        #     return str
        # result = [""] * len(str)
        # m = {}
        # for s in str:
        #     m[s] = m.get(s, 0) + 1
        # m_array = list(m.items())
        # sorted_m_array = sorted(m_array, key = lambda t: t[1], reverse=True)

        # start = 0
        # for item in sorted_m_array:
        #     count = item[1]
        #     char = item[0]
        #     cur = start
        #     while count > 0:
        #         if cur >= len(str) or result[cur] != "": #either out of boundary or slot is taken means fails
        #             return ""
        #         result[cur] = char
        #         count -= 1
        #         cur = cur + k
        #     # start += 1
        #     for i in xrange(len(result)):
        #         if result[i] == "":
        #             start = i
        #             break

        # return "".join(result)
