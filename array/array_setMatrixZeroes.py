"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 解题思路：分别记录两个向量x, y，保存行和列是否有0，再次遍历数组时查询对应的行和列然后修改值。
        # one improvement is to use matrix[i][0] and matrix[0][j] as markers

        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]

        for i in xrange(rownum):
            for j in xrange(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in xrange(rownum):
            for j in xrange(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

