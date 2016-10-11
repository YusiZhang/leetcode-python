import bisect
import sys
class Solution(object):
    def max_sum_no_more_than_k(self, a, k):
        cum_list = [0]
        cum = 0
        max_so_far = -sys.maxint
        for i in range(len(a)):
            cum += a[i]
            cum_j_index = bisect.bisect_left(cum_list, cum - k)
            if cum_j_index < len(cum_list):
                max_so_far = max(max_so_far, cum - cum_list[cum_j_index])
            bisect.insort(cum_list, cum)

        return max_so_far

    def maxSumSubmatrix(self, matrix, k):
        if not matrix:
            return 0
        row_num = len(matrix)
        max_so_far = -sys.maxint
        columns = zip(*matrix)
        for l in range(len(columns)):
            current = [0] * row_num
            for column in columns[l:]:
                current = map(int.__add__, current, column)
                ans = self.max_sum_no_more_than_k(current, k)
                max_so_far = max(max_so_far, ans)
        return max_so_far