class RangeSum2DMutable(object):
    def __init__(self, matrix):
        if not matrix:
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.myMatrix = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.bit = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff = val - self.myMatrix[row][col]
        self.myMatrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumCorner(self, row, col):
        res = 0
        i = row + 1
        while i:
            j = col + 1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) \
               - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)


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
    update(3, 2, 2)
    sumRegion(2, 1, 4, 3) -> 10
    """
    numMatrix = RangeSum2DMutable(matrix)
    print numMatrix.sumRegion(2, 1, 4, 3)
    numMatrix.update(3, 2, 2)
    print numMatrix.sumRegion(2, 1, 4, 3)
