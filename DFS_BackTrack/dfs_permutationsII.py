__author__ = 'yusizhang'
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        # key point1, this array need to be sorted. just like w/o duplicate combination
        nums.sort()
        prev = None
        result = []

        for i in range(len(nums)):
            # key point2, store the previous number, skip if the same.
            # avoid [1,1,4,5] --> [1,1,4,5] and [1,1,4,5]
            if nums[i] == prev:
                continue
            prev = nums[i]
            for j in self.permuteUnique(nums[:i], nums[i+1:]):
                result.append(nums[i] + j)

        return result
