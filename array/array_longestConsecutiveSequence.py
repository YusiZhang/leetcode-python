__author__ = 'yusizhang'
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Show Company Tags
Hide Tags
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        nums_set = set(nums)
        length = 1
        for num in nums:
            lower = num - 1
            while lower in nums_set:
                nums_set.remove(lower)
                lower -= 1
            upper = num + 1
            while upper in nums_set:
                nums_set.remove(upper)
                upper += 1
            length = max(length, upper - lower - 1)
        return length
