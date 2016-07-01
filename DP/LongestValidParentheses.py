class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP solution
        if not s or len(s) <= 1:
            return 0
        curMax = 0
        dp_longest = [0] * len(s)
        for i in xrange (1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp_longest[i] = dp_longest[i-2] + 2 if i - 2 >= 0 else 2
                    curMax = max(dp_longest[i], curMax)
                else: #s[i] == ")", combine the previous length
                    if i - dp_longest[i-1] - 1 >= 0 and s[i-dp_longest[i-1]-1] == "(":
                        dp_longest[i] = dp_longest[i-dp_longest[i-1]-2] + (dp_longest[i-1] + 2) if (i-dp_longest[i-1]-2 >= 0) else dp_longest[i-1] + 2
                        curMax = max(dp_longest[i], curMax)
            # else if s[i] == "(", skip it, because it cannot be a valid parentheses. so the dp[i] must be 0
        return curMax

        def longestValidParentheses_stack(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack solution
        if not s or len(s) <= 1:
            return 0
        indices = []
        indices.append(-1) # dummy node, to calculate length including the root/first "("
        curMax = 0
        for i in xrange(len(s)):
            if s[i] == "(":
                indices.append(i)
            else: # s[i] == ")"
                indices.pop()
                if indices == []:
                    indices.append(i)
                else:
                    curMax = max(curMax, i-indices[-1])
        return curMax

        

        
"""dp
 int longestValidParentheses(string s) {
            if(s.length() <= 1) return 0;
            int curMax = 0;
            vector<int> longest(s.size(),0);
            for(int i=1; i < s.length(); i++){
                if(s[i] == ')'){
                    if(s[i-1] == '('){
                        longest[i] = (i-2) >= 0 ? (longest[i-2] + 2) : 2;
                        curMax = max(longest[i],curMax);
                    }
                    else{ // if s[i-1] == ')', combine the previous length.
                        if(i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                            longest[i] = longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                            curMax = max(longest[i],curMax);
                        }
                    }
                }
                //else if s[i] == '(', skip it, because longest[i] must be 0
            }
            return curMax;
        }
"""
        