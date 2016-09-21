__author__ = 'yusizhang'
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 跟subtset唯一区别就是只有当count/depth 等于K时才加入结果中
        self.result = []
        self.count = 0
        self.dfs(1, [], self.count, k, n)

    def dfs(self, start, valuelist, count, k, n):
        if count == k:
            self.result.append(valuelist)
            return
        # this is the key part of all dfs solution for permutation and combination questions
        for i in range(start, n + 1):
            self.dfs(start, valuelist + [i], count + 1)
