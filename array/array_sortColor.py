"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # revisit this quesiton with one pass solution next time
        # https://leetcode.com/discuss/17000/share-my-one-pass-constant-space-10-line-solution

        count_red = 0
        count_white = 0
        count_blue = 0

        for color in nums:
            if color == 0:
                count_red += 1
            elif color == 1:
                count_white += 1
            elif color == 2:
                count_blue += 1
            else:
                raise ValueError("wrong color in the input array")

        for i in range(len(nums)):
            if count_red > 0:
                nums[i] = 0
                count_red -= 1
                continue
            if count_white > 0:
                nums[i] = 1
                count_white -= 1
                continue
            if count_blue > 0:
                nums[i] = 2
                count_blue -= 1
                continue
