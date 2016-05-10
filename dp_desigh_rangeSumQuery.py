__author__ = 'yusizhang'


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        # sum range dp solution
        # sum[i] means sum from 0 to i inclusively.
        # ai...aj sum will be sum[j] - sum[i-1]
        # if i = 0, a0...ai will be sum[j]. No need to minus sum[0-1]
        """
        self.sums_dp = [None] * len(nums)
        if len(nums) > 0:
            self.sums_dp[0] = nums[0]
            for i in range(1, len(nums)):
                self.sums_dp[i] = self.sums_dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums_dp[j]
        else:
            return self.sums_dp[j] - self.sums_dp[i - 1]


    # Your NumArray object will be instantiated and called as such:
    # numArray = NumArray(nums)
    # numArray.sumRange(0, 1)
    # numArray.sumRange(1, 2)
