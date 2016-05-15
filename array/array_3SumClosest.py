"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Show Company Tags
Hide Tags
"""

import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        K sum's typical two pointer solution
        """
        nums.sort()
        diff = sys.maxint
        result = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(sum - target)
                if curr_diff < diff:
                    diff = curr_diff
                    result = curr_sum
                if curr_sum == target:
                    return result
                elif curr_diff < target:
                    left += 1
                else:
                    right -= 1

        return result
