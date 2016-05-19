"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lenNum = len(nums)
        if lenNum < 4:
            return []
        # nums need to be sorted
        nums.sort()
        result = set()
        dict = {}
        for p in xrange(lenNum):
            for q in xrange(p+1, lenNum):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p] + nums[q]] = [(p, q)]
                else:
                    dict[nums[p] + nums[q]].append((p,q))

        for i in xrange(lenNum):
            for j in xrange(i+1, lenNum-2):
                if target - nums[i] - nums[j] in dict:
                    for k in dict[target-nums[i]-nums[j]]:
                        if k[0] > j:
                            result.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))

        return [list(i) for i in result]