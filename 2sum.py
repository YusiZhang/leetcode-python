__author__ = 'yusizhang'
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            value = nums[i]
            if target - value in dict:
                return [i, dict[target - value]]
            dict[nums[i]] = i