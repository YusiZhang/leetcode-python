__author__ = 'yusizhang'
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if it is non-positive, ignore it
        # if it is positive, A[i] = x, then we put it to A[x-1]. Bucket sort
        if not nums:
            return 1
        for i in range(len(nums)):
            # nums[i] == i means the number is already in position
            # nums[i] != nums[nums[i]-1] to avoid infinite loop
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
