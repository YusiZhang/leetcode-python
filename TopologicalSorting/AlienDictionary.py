"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dependencyMap = {}
        degree = {}
        res = ""
        if not words or len(words) == 0:
            return res
        # todo use python way to short this block
        for word in words:
            for c in word:
                degree[c] = 0

        for i in xrange(len(words)-1):
            cur  = words[i]
            next = words[i+1]
            length = min(len(cur), len(next))
            for j in xrange(length):
                c1 = cur[j]
                c2 = next[j]
                if c1 != c2:
                    cur_set = set()
                    if c1 in dependencyMap:
                        cur_set = dependencyMap[c1]
                    if c2 not in cur_set:
                        cur_set.add(c2)
                        dependencyMap[c1] = cur_set
                        degree[c2] = degree[c2]+1
                    break

        q = collections.deque()
        for c in degree:
            if degree[c] == 0:
                q.append(c)
        while q:
            c = q.popleft()
            res += c
            if c in dependencyMap:
                for c2 in dependencyMap[c]:
                    degree[c2] = degree[c2] - 1
                    if degree[c2] == 0:
                        q.append(c2)
        if len(res) != len(degree):
            return ""
        return res
