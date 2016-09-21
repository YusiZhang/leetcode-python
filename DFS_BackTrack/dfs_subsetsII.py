__author__ = 'yusizhang'
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # subset or combination uses dfs!
        # subset remember to sort the nums first
        self.result = []
        nums.sort()
        self.dfs(nums, 0, 0, [])
        return self.result

    def dfs(self, nums, depth, start, valueList):
        # add the valueList first!
        self.result.append(valueList)
        if depth == len(nums):
            return
        for i in range(start, len(nums)):
            # don't forget to add i!=start.
            # it is very okay to skip the first one.
            if nums[i] == nums[i-1] and i!=start:
                continue
            # since we only add nums[i] at the time we pass in to next level dfs call
            # no need to remove the last nums[i] from the valueList
            # not like what Nine Chapter answer does
            self.dfs(nums, depth+1, start+1, valueList+[nums[i]])