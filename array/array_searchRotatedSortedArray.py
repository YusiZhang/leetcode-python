__author__ = 'yusizhang'
class Solution(object):
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[start]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target: return start
        if nums[end] == target: return end
        return -1

