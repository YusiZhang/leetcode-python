__author__ = 'yusizhang'
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        n = len(matrix)
        m = len(matrix[0])
        top, right, bottom, left = 0, m-1, n-1, 0
        result = []
        direction = 0
        # 0 left to right, 1 top to bottom, 2 right to left, 3 bottom to top

        while top <= bottom and left <= right:
            if direction == 0:
                for i in xrange(left, right+1):
                    result.append(matrix[top][i])
                top += 1
            if direction == 1:
                for i in xrange(top, bottom+1):
                    result.append(matrix[i][right])
                left -= 1
            if direction == 2:
                for i in xrange(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if direction == 3:
                for i in xrange(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return result