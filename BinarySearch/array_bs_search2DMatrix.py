"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # BS in row index to find the protential row index
        # BS in that found row to determine existance.

        m = len(matrix); n = len(matrix[0])
        if m == 0 and n == 0:
            return False
        if matrix[0][0] > target:
            return False
        if matrix[m-1][n-1] < target:
            return False

        start, end, row_index = 0, m - 1, 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[start][0] == target:
            return True
        if matrix[end][0] == target:
            return True
        if matrix[start][0] < target and target < matrix[end][0]:
            row_index = start
        # don't forget this case!!!!
        # [[1,3,5,7],[10,11,15,17]] target:11
        if matrix[end][0] < target:
            row_index = end

        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[row_index][start] == target:
            return True
        if matrix[row_index][end] == target:
            return True

        return False
