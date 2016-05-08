class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        prev = []
        for i in range(0,numRows):
            current = []
            for j in xrange(0,i):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append(prev[j-1] + prev[j])
            prev = current
            result.append(current)
        return result

if __name__ == '__main__':
    print Solution().generate(5)