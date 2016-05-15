"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # https://leetcode.com/discuss/46104/simple-java-solution-in-o-n-without-extra-space
        """
        Numbers:     2    3    4     5
        Lefts:            2  2*3 2*3*4
        Rights:  3*4*5  4*5    5
        """
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result

