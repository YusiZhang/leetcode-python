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
        
        row = len(matrix); column = len(matrix[0])
        if row == 0 and column == 0:
            return False
        if matrix[0][0] > target:
            return False
        if matrix[row-1][column-1] < target:
            return False
            
        start, end, row_index = 0, row - 1, 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False
            
        start, end = 0, column - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[row][start] == target:
            return True
        if matrix[row][end] == target:
            return True
        
        return False
        