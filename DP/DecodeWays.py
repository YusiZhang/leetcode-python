# This is very similar to climbing stairs questions.
"""
dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 1.
I then check one digit and two digit combination and save the results along the way.
In the end, dp[n] will be the end result.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in xrange(2, n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if first >= 1 and first <= 9:
                dp[i] += dp[i-1]
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]

        return dp[n]

"""
public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if(first >= 1 && first <= 9) {
               dp[i] += dp[i-1];
            }
            if(second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}
"""