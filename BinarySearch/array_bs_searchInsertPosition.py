"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        # first position >= target
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        start, end = 0, length - 1
        if nums[start] > target:
            return start
        if nums[end] < target:
            return end + 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if nums[start] < target and target < nums[end]:
            return start + 1

        return None

# More concise colution
class Solution2:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0

        start, end = 0, len(A) - 1
        # first position >= target
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)