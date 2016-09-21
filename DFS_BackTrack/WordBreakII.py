class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.findWords(0, len(s), s, wordDict, {})

    def findWords(self, start, end, s, wordDict, cache):
        if start in cache:
            return cache[start]
        cache[start] = []
        candidate = ''
        current = start
        while current < end:
            candidate += s[current]
            current += 1
            if candidate in wordDict:
                if current == end:
                    cache[start].append(candidate)
                else:
                    for x in self.findWords(current, end, s, wordDict, cache):
                        cache[start].append(candidate + ' ' + x)
        return cache[start]


if __name__ == '__main__':
    s= "catsanddog"
    dic = ["cat", "cats", "and", "sand", "dog"]
    solution = Solution()
    print solution.wordBreak(s, dic)