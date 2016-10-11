import sys


class Solution(object):
    def shortestWordDistanceBetter(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance, p1, p2 = sys.maxint, -1, -1
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                if word1 == word2:
                    p1 = p2
                p2 = i
            if p1 != -1 and p2 != -1:
                distance = min(distance, abs(p1-p2))
        return distance

    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words or not word1 or not word2:
            return -1
        dic = {}
        for index, word in enumerate(words):
            if word in dic:
                dic[word].append(index)
            else:
                dic[word] = [index]

        indices_word1 = dic[word1]
        indices_word2 = dic[word2]

        res = sys.maxint
        for i in range(len(indices_word1)):
            for j in range(len(indices_word2)):
                if word1 == word2 and indices_word1[i] == indices_word2[j]:
                    continue
                res = min(res, abs(indices_word1[i] - indices_word2[j]))

        return res

if __name__ == '__main__':
    s = Solution()
    words = ["a","a"]
    word1 = "a"
    word2 = "a"

    s.shortestWordDistance(words, word1, word2)

