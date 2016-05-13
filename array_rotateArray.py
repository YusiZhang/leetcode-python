__author__ = 'yusizhang'
"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - k % n
        # all rotate questions are similar, the rotate image question also needs to
        # rotate the matrix to 转置矩阵 then reverse each column
        # so if quesiton is from A rotate to B, think if you can achieve that via A - C - B
        nums = self.reverse(nums, 0, n)
        nums = self.reverse(nums, 0, n - k)
        nums = self.reverse(nums, n - k, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x], nums[start + end - x - 1] = nums[start + end - x - 1], nums[x]

        return nums
