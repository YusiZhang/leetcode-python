# coding=utf-8
__author__ = 'yusizhang'
import sys
class Solution(object):
    """
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

    For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
    the contiguous subarray [4,−1,2,1] has the largest sum = 6.
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = [0] * (len(nums) + 1)
        sum[0] = 0
        for i in range(1, len(nums) + 1):
            sum[i] = sum[i-1] + nums[i - 1]
        minSum = sum[0]
        maxSumDiff = -1 - sys.maxint
        for i in range(1, len(nums)+1):
            minSum = min(minSum, sum[i])
            maxSumDiff = max(maxSumDiff, sum[i] - minSum)
        return maxSumDiff if maxSumDiff >0 else max(nums)

    # This is a more concise solution
    def maxSubArray2(self, nums):
        minSum = 0
        sum = 0
        maxDiff = -1 - sys.maxint
        for i in range(len(nums)):
            sum += nums[i]
            maxDiff = max(maxDiff, sum - minSum)
            minSum = min(minSum, sum)
        return maxDiff