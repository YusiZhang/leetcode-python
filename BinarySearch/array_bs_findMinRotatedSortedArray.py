__author__ = 'yusizhang'
class Solution(object):
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    You may assume no duplicate exists in the array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]

        while start + 1 < end:
            mid = start + (end - start) / 2
            # I should only consider if
            # 1. if nums[mid] > nums[start], then else
            # 2. if nums[mid] < nums[end], then else
            if nums[mid] > nums[end]:
                # start to mid is sorted, and nums[end] definitely less than nums[start].
                # so you only need to search from mid to end
                start = mid
            else:
                # mid to end is sorted, and mid is less than end, so at lease the mid is relatively small one.
                # so you only need to search from start to mid
                end = mid
        return min(nums[start], nums[end])