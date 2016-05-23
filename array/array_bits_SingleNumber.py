"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# 异或:相异为1,相同为0
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return None
        ans = nums[0]
        for i in xrange(1, len(nums)):
            ans = ans ^ nums[i]

        return ans