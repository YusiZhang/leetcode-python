"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        pattern_length = len(pattern)
        word_array = str.split(" ")
        word_array_length = len(word_array)
        if pattern_length != word_array_length:
            return False
        word_pattern_dict = {}
        for i in xrange(word_array_length):
            if word_array[i] not in word_pattern_dict:
                if pattern[i] in word_pattern_dict.values():
                    return False
                else:
                    word_pattern_dict[word_array[i]] = pattern[i]
            else:
                if word_pattern_dict[word_array[i]] != pattern[i]:
                    return False
        return True

    # learn how to use zip method in python!!
    def wordPattern2(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        ptnDict, wordDict = {}, {}
        # zip will return a tuple in pairs
        for ptn, word in zip(pattern, words):
            if ptn not in ptnDict:
                ptnDict[ptn] = word
            if word not in wordDict:
                wordDict[word] = ptn
            if wordDict[word] != ptn or ptnDict[ptn] != word:
                return False
        return True
        