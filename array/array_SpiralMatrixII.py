"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Show Tags
Hide Similar Problems
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n or n == 0:
            return []
        matrix = [[0 for i in xrange(n)] for i in xrange(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        direction = 0
        current = 1

        while left <= right and top <= bottom:
            if direction == 0: # left -> right
                for i in xrange(left, right+1):
                    matrix[top][i] = current
                    current += 1
                top += 1
            if direction == 1: # top -> bottom
                for i in xrange(top, bottom+1):
                    matrix[i][right] = current
                    current += 1
                right -= 1
            if direction == 2: # right -> left
                for i in xrange(right, left-1, -1):
                    matrix[bottom][i] = current
                    current += 1
                bottom -= 1
            if direction == 3: # bottom -> top
                for i in xrange(bottom, top-1, -1):
                    matrix[i][left] = current
                    current += 1
                left += 1
            direction = (direction + 1) % 4

        return matrix