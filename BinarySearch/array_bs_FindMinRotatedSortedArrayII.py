"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start = 0
        # end = len(nums) - 1
        # while start < end and nums[start] >= nums[end]:
        #     mid = (start + end) / 2
        #     if nums[mid] > nums[start]:
        #         start = mid + 1
        #     elif nums[mid] < nums[end]:
        #         end = mid
        #     else:
        #         start += 1
        #
        # return nums[start]
        if not nums or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == nums[end]:
                # if mid equals to end, that means it is fine to remove end
                # the smallest element won't be removed
                # because end won't be larger than the start.
                end -= 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start = mid

        return min(nums[start], nums[end])
