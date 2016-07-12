"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # y = len(matrix[0]) - 1
        # def binSearch(nums, low, high):
        #     while low <= high:
        #         mid = (low + high) / 2
        #         if nums[mid] > target:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     return high
        # for x in range(len(matrix)):
        #     y = binSearch(matrix[x], 0, y)
        #     if matrix[x][y] == target:
        #         return True
        # return False
        


#这道题是经典题, 我在微软和YELP的onsite和电面的时候都遇到了. 
#从右上角开始, 比较target 和 matrix[i][j]的值. 如果小于target, 则该行不可能有此数,  所以i++; 如果大于target, 则该列不可能有此数, 所以j--. 遇到边界则表明该矩阵不含target.

        if matrix == [] or matrix[0] == []:
            return False
            
        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False
        