class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        for i in xrange(len(s)):
        	len1 = self.expandAroundCenters(s, i, i)
        	len2 = self.expandAroundCenters(s, i, i+1)
        	length = max(len1, len2)
        	# very handy way to get the start and end index 
        	# when you know the length of whole substring, and the center of the substring
        	if length > end - start:
        		start = i - (length-1)/2 
        		end = i + (length)/2

        return s[start, end+1]

    def expandAroundCenters(self, s, left, right):
    	L = left
    	R = right
    	while L >= 0 and R < len(s) and s[L] == s[R]:
    		L -= 1
    		R -= 1
    	return R - L -1 
    	#when exit while loop, the L is already -1, and R is already +1
    	# so we need to fix it by -1 to get the actual length
