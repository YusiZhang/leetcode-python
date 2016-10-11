"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
"""
"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s :
            return True
            
        if not wordDict:
            return False
        
        maxLength = len(max(wordDict, key=lambda x: len(x)))
        canSegment = [False for _ in range(len(s)+1)]
        canSegment[0] = True
        
        for i in range(len(s)+1):
            lastWordLength = 1
            while lastWordLength <= maxLength and lastWordLength <= i:
                if not canSegment[i-lastWordLength]:
                    lastWordLength += 1
                    continue
                word = s[i-lastWordLength:i]
                if word in wordDict:
                    canSegment[i] = True
                    break
                lastWordLength += 1
                
        return canSegment[len(s)]
