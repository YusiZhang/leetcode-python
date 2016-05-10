__author__ = 'yusizhang'

class Solution(object):
    """
    Given an index k, return the kth row of the Pascal's triangle.

    For example, given k = 3,
    Return [1,3,3,1].

    Note:
    Could you optimize your algorithm to use only O(k) extra space?
    """
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1 # e.g. when k = 3, it means the 4th line in the triangle
        if rowIndex == 0:
            return []
        result = []
        result.append(1)

        for i in range(1, rowIndex):
            tmp = [None] * (i+1)
            tmp[0] = result[0]
            tmp[i] = result[i-1]
            for j in range(1, i):
                tmp[j] = result[j-1] + result[j]
            result = tmp
            tmp = None
        return result
if __name__ == '__main__':
    print Solution().getRow(5)
