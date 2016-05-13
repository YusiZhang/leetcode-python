__author__ = 'yusizhang'
"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k == 0:
            return False

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            dict[nums[i]] = i
            # key point! As long as the len of the dict is less then k,
            # we can safely say the found duplicates' distance are at most k
            if len(dict) > k:
                dict.pop(nums[i-k], None)

        return False
