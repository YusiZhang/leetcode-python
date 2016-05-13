__author__ = 'yusizhang'
"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        result = []

        for i in range(len(nums)):
            # leading with nums[i], all combinations from nums without nums[i],
            # and they can be constructed from
            # permute from nums without nums[i].
            for j in self.permute(nums[:i], nums[i+1]):
                result.append(nums[i] + j)

        return result
