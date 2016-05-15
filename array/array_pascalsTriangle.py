class Solution(object):
    """
    Given numRows, generate the first numRows of Pascal's triangle.
    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    Show Company Tags
    Show Tags
    Show Similar Problems
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        result.append([1])

        for i in range(1, numRows):
            current = [None] * (i + 1)
            prev = result[i-1]
            current[0] = prev[0]
            current[i] = prev[i-1]
            for j in range(1, i):
                current[j] = prev[j-1] + prev[j]
            result.append(current)
        return result


if __name__ == '__main__':
    print Solution().generate(5)