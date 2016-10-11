class Solution:
 # @param A, B: Two string.
 # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        f = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        # f[i][j] represents the length of common substring ending with i in A and ending with j in B
        res = 0
        for i in range (1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = 0
                res = max(res, f[i][j])
        
        return res

 
 
 """
 Given two strings, find the longest common substring.

Return the length of it.

 Notice

The characters in substring should occur continuously in original string. This is different with subsequence.
"""