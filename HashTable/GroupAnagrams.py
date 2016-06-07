"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            word_dict[sortedWord] = word if sortedWord not in word_dict else word_dict[sortedWord] + [word]

        result = []

        for key in word_dict:
            result.append(word_dict[key])

        return result
