"""
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.backtrack(res, word, 0, "", 0)
        return res

    def backtrack(self, res, word, pos, cur, count):
        if pos == len(word):
            if count > 0:
                cur += str(count)
            res.append(cur)
        else:
            self.backtrack(res, word, pos + 1, cur, count + 1)
            self.backtrack(res, word, pos + 1, cur + (str(count) if count > 0 else "") + word[pos], 0)


"""
The idea is: for every character, we can keep it or abbreviate it.
To keep it, we add it to the current solution and carry on backtracking.
To abbreviate it, we omit it in the current solution,
but increment the count,
which indicates how many characters have we abbreviated.
When we reach the end or need to put a character in the current solution,
and count is bigger than zero, we add the number into the solution.

"""