# coding=utf-8
__author__ = 'yusizhang'
class Solution(object):
    """
    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.
    """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer solution
        left, right = 0, 0
        length = len(nums) + 1
        sum = 0
        for left in range(len(nums)):
            while right < len(nums) and sum < s:
                sum += nums[right]
                right += 1
            if sum >= s:
                # Since the right has already been added one more in the while loop
                # So that I don't need to run right - left + 1 to get the length
                length = min(length, right - left)
            sum -= nums[left]
        if length == len(nums) + 1:
            return 0
        return length
        # Solution for NlogN
        # https://leetcode.com/discuss/35378/solutions-java-with-time-complexity-nlogn-with-explanation

if __name__ == '__main__':
    print Solution().minSubArrayLen(7, [2,3,1,2,4,3])