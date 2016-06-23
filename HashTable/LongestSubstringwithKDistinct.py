"""
use two pointer to keep track distinct characters
within the slide window
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m = {}
        left = 0
        maxlen = 0
        for i in xrange(len(s)):
        	m[s[i]] = m.get(s[i], 0) + 1
        	while len(m) > k:
        		leftChar = s[left]
        		if leftChar in m:
        			m[leftChar] -= 1
        			if m[leftChar] == 0:
        				m.pop(leftChar)
        		left += 1
        	maxlen = max(maxlen, i - left + 1)

        return maxlen

        # distinct = {}
        # maxlen = 0
        # left = 0
        # if k == 0:
        #     return 0
        # for right, char in enumerate(s):
        #     if len(distinct) == k and char not in distinct:
        #         left = min(distinct.values()) + 1
        #         distinct.pop(s[left-1])
        #     distinct[char] = right
        #     maxlen = max(maxlen, right - left + 1)
            
        # return maxlen
