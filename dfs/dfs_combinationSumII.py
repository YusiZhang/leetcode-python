# coding=utf-8
__author__ = 'yusizhang'
"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 此题与Combination Sum I最大的区别是每个candidate只能使用一次
        if len(candidates) == 0 or not candidates:
            return []

        candidates.sort()
        self.result = []
        self.dfs(candidates, target, 0, [])

        return self.result
    """
   构建DFS前问自己：
   1. candidate可否重用？
   2. 是否要求unique combination？
   构建DFS参数时记得：
   1. candidates,
   2. target?
   3. start. 一般candidate不可重用时还需要加入count or depth已记录当前状态
   4. 中间过渡变量 valuelist
   """
    def dfs(self, candidates, target, start, valuelist):
        if target == 0 and valuelist not in self.result:
            self.result.append(valuelist)
            # don't forget return...
            return

        length = len(candidates)
        for i in range(start, length):
            # 因为candidates都是正数
            if target < candidates[i]:
                return
            # 由于每个数字只能使用一次，所以下一层dfs要传入i+1
            self.dfs(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])
