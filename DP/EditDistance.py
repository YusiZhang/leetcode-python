class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        # state
        f = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1) + 1)]
        # init
        f[0][0] = 0
        for i in range(1, len(word1)+1):
            f[i][0] = f[i-1][0] + 1
        for j in range(1, len(word2)+1):
            f[0][j] = f[0][j-1] + 1
        
        # func
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                f[i][j] = min(f[i][j-1]+1, f[i-1][j]+1, f[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
            
        # result
        return f[len(word1)][len(word2)]

        """
        解题思路：这道题是很有名的编辑距离问题。用动态规划来解决。
        状态转移方程是这样的：dp[i][j]表示word1[0...i-1]到word2[0...j-1]的编辑距离。
        而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。同理dp[0][i]也是如此，等于i，
        因为只需做i次插入操作就可以了。dp[i-1][j]变到dp[i][j]需要加1，
        因为word1[0...i-2]到word2[0...j-1]的距离是dp[i-1][j]，而word1[0...i-1]到word1[0...i-2]需要执行一次删除，
        所以dp[i][j]=dp[i-1][j]+1；同理dp[i][j]=dp[i][j-1]+1，因为还需要加一次word2的插入操作。如果word[i-1]==word[j-1]，
        则dp[i][j]=dp[i-1][j-1]，如果word[i-1]!=word[j-1]，那么需要执行一次替换replace操作，
        所以dp[i][j]=dp[i-1][j-1]+1，以上就是状态转移方程的推导。
        """
        
"""
class Solution: 
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        # state
        f = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1) + 1)]
        # init
        f[0][0] = 0
        for i in range(1, len(word1)+1):
            f[i][0] = f[i-1][0] + 1
        for j in range(1, len(word2)+1):
            f[0][j] = f[0][j-1] + 1
        
        # func
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                f[i][j] = min(f[i][j-1]+1, f[i-1][j]+1, f[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
            
        # result
        return f[len(word1)][len(word2)]
"""