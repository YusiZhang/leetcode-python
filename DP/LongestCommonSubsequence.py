class Solution:
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        f = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        f[0][0] = 0
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                f[i][j] = max(f[i-1][j], f[i][j-1]) if A[i-1] != B[j-1] else ( f[i-1][j-1] + 1)
                
        return f[len(A)][len(B)]
        
