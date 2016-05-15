# coding=utf-8
__author__ = 'yusizhang'
class Solution(object):
    """
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
    The algorithm should run in linear time and in O(1) space.
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None
        for num in nums:
            if candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif candidate1 == num:
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
        if count1 > len(nums) / 3.0 and count2 > len(nums) / 3.0:
            return [candidate1, candidate2]
        if count1 > len(nums) / 3.0 and not count2 > len(nums) / 3.0:
            return [candidate1]
        if count2 > len(nums) / 3.0 and not count1 > len(nums) / 3.0:
            return [candidate2]
        return []