class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        # f[i][j][t] 表示前i个元素中，不包含i本身，取j个元素，sum是t
        if not A:
        	return 0
        n = len(A)
        f = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(n + 1)]
        for i in range(n+1):
        	f[i][0][0] = 1

        for i in range(1, n+1):
        	for j in range(1, k+1):
        		for t in range(target+1):
        			if t >= A[i-1]:
        				f[i][j][t] = f[i-1][j-1][t-A[i-1]]
        			f[i][j][t] += f[i-1][j][t]

        return f[n][k][target]



"""
public int  kSum(int A[], int k, int target) {
        int n = A.length;
        int[][][] f = new int[n + 1][k + 1][target + 1];
        for (int i = 0; i < n + 1; i++) {
            f[i][0][0] = 1;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k && j <= i; j++) {
                for (int t = 1; t <= target; t++) {
                    f[i][j][t] = 0;
                    if (t >= A[i - 1]) {
                        f[i][j][t] = f[i - 1][j - 1][t - A[i - 1]];
                    }
                    f[i][j][t] += f[i - 1][j][t];
                } // for t
            } // for j
        } // for i
        return f[n][k][target];
    }
"""