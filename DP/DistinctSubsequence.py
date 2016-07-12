"""
 Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3. 
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s = len(s)
        len_t = len(t)
        
        # dp =  [[0] * (len_s+1)] * (len_t+1)
        dp = [[ 0 for _ in range(len_s+1)] for _ in range(len_t+1)]
        for i in xrange(len_s+1):
            dp[0][i] = 1 #target is "", but source has something
            
        for t_index in xrange(1, len_t+1):
            for s_index in xrange(1, len_s+1):
                if t[t_index-1] != s[s_index-1]:
                    dp[t_index][s_index] = dp[t_index][s_index-1]
                else:
                    dp[t_index][s_index] = dp[t_index][s_index-1] + dp[t_index-1][s_index-1]
        
        return dp[len_t][len_s]
        
        
"""
public int numDistinct(String S, String T) {
    int sl = S.length();
    int tl = T.length();

    int [][] dp = new int[tl+1][sl+1];

    for(int i=0; i<=sl; ++i){
        dp[0][i] = 1;
    }

    for(int t=1; t<=tl; ++t){

        for(int s=1; s<=sl; ++s){
            if(T.charAt(t-1) != S.charAt(s-1)){
                dp[t][s] = dp[t][s-1];
            }else{
                dp[t][s] = dp[t][s-1] + dp[t-1][s-1];
            }
        }   
    }

    return dp[tl][sl];
}
"""
        