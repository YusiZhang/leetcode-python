__author__ = 'yusizhang'
"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 组合求解类都用DFS
        # Remember to sort the nums first!
        nums.sort()
        self.result = []
        self.dfs(0,0,[],nums)
        return self.result

    def dfs(self, depth, start, valueList, nums):
        self.result.append(valueList)
        if depth == len(nums):
            return
        for i in range(start, len(nums)):
          # note: i+1!!
            self.dfs(depth+1, i+1, valueList + [nums[i]], nums)