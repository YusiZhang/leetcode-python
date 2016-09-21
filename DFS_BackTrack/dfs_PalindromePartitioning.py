# coding=utf-8
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0 or not s:
            return []

        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, stringlist):
        if len(s) == 0:
            self.result.append(stringlist)
            return

        for i in range(1, len(s)+1):
            # set中string全部回文的成立前提，是至少要求已取出来的substring是回文的。
            if self.isPalindrome(s[:i]):
                # nums[len(nums):] 不会越界
                self.dfs(s[i:], stringlist + [s[:i]])


    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True