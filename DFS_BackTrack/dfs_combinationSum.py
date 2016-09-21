# coding=utf-8
__author__ = 'yusizhang'
"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0 or not candidates:
            return []

        # most of combination questions need to sort the candidates first
        candidates.sort()
        # remember to define self.result if the question need a returned result
        self.result = []

        # call dfs here...
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
        """
        DFS函数第一步一般先判断跳出/返回条件
        """
        if target == 0:
            self.result.append(valuelist)
            return

        length = len(candidates)
        for i in range(start, length):
            # 若有需要也要记得先判断循环跳出条件
            # 因为candidates都是正数
            if target < candidates[i]:
                return
            # 每个数字可以重复使用，所以下一层dfs不需要传入i+1
            self.dfs(candidates, target - candidates[i], i, valuelist+[candidates[i]])

