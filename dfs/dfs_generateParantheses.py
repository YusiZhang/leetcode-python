# coding=utf-8
__author__ = 'yusizhang'
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []

        self.result = []
        self.dfs(0,0,"",n)

        return self.result

    def dfs(self, left, right, string, n):
        if left == n and right == n:
            self.result.append(string)
            return

        if left < n:
            self.dfs(left+1, right, string + "(", n)

        if right < left:
            self.dfs(left, right+1, string + ")", n)
