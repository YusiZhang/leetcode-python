"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # f[i] 表示前i个字母，最少可以被分割为多少个回文串
        if not s:
            return 0
        
        # prepare
        isPalindrome = self.getIsPalindrome(s)
        
        # init
        f = [sys.maxint for _ in range(len(s)+1)]
        f[0] = 0
        
        # main
        for i in range(1, len(s)+1):
            for j in range(i):
                if isPalindrome[j][i-1]:
                    f[i] = min(f[i], f[j] + 1)
        
        return f[len(s)] - 1
        
    def getIsPalindrome(self, s):
        isPalindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            isPalindrome[i][i] = True
        
        for i in range(len(s) - 1):
            isPalindrome[i][i+1] = (s[i] == s[i+1])
            
        for length in range(2, len(s)):
            for start in range(len(s) - length):
                isPalindrome[start][start+length] = isPalindrome[start+1][start + length -1] and s[start] == s[start + length]
                
        return isPalindrome



        