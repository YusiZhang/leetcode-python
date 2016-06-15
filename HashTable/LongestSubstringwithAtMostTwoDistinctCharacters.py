"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""

"""
Idea is simple. Maintain left to right window. 
If third char encountered, remove the char 
which has the lowest position value and update left pointer to the lowest position + 1. 
This solution can be easily extend to k distinct chars.
"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct = {}
        maxlen = 0
        left = 0
        for right, char in enumerate(s):
        	if len(distinct == 2) and char not in distinct:
        		left = min(distinct.values()) + 1
        		distinct.pop(s[left-1])
        	distinct[char] = right
        	maxlen = max(maxlen, right - left + 1)

        return maxlen