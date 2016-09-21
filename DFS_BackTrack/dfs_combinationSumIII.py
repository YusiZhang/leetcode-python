# coding=utf-8
__author__ = 'yusizhang'
"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:
Input: k = 3, n = 7

Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9

Output:
[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 找到1-9所有个数为k的subset，再一次判断其sum是否为n
        nums = [1,2,3,4,5,6,7,8,9]
        self.result = []
        self.dfs(nums, k, n, 0, [])

        return self.result

    def dfs(self, nums, k, n, start, valuelist):
        sum = 0
        if len(valuelist) == k:
            for value in valuelist:
                sum += value
            if sum == n:
                self.result.append(valuelist)

        for i in range(start, len(nums)):
            self.dfs(nums, k, n, i+1, valuelist + [nums[i]])