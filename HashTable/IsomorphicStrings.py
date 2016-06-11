"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
        	d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
        	d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    # why?
    def isIsomorphic2(self, s, t):
    	d1 , d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
    	for i in xrange(len(s)):
    		if d1[ord(s[i])] != d2[ord(t[i])]:
    			return False
    		d1[ord(s[i])] = i + 1
    		d2[ord(t[i])] = i + 1
    	return True

    """
    使用两个哈希表sourceMap和targetMap维护两个字符串中字符的映射关系。

	sourceMap[ t[x] ] = s[x]

	targetMap[ s[x] ] = t[x]

	当出现映射不一致的情形时，返回False

	否则返回True
    """
    def isIsomorphic3(sefl, s, t):
    	d_s = {}, d_t = {}
    	for i in xrange(len(s)):
    		if s[i] in d_s and d_s[s[i]] != t[i]:
    			return False
    		if t[i] in d_t and d_t[t[i]] != s[i]:
    			return False
    		d_s[s[i]] = t[i]
    		d_t[t[i]] = s[i]
    	return True



