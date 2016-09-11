class RangeSum2DImmutable(object):
    def __init__(self, _matrix):
        """
        initialize your data structure here.
        :type _matrix: List[List[int]]
        """
        if not _matrix:
            return
        m, n = len(_matrix), len(_matrix[0])
        self.sums = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.sums[i][j] = _matrix[i - 1][j - 1] + self.sums[i - 1][j] + self.sums[i][j - 1] - self.sums[i - 1][
                    j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][
            col1 - 1]


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    """
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
    """
    numMatrix = RangeSum2DImmutable(matrix)
    print numMatrix.sumRegion(2, 1, 4, 3)
    print numMatrix.sumRegion(1, 1, 2, 2)
