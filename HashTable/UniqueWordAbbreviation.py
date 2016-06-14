class ValidWordAbbr(object):
    # static_element = {} this is static var belongs to the class
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrDict = {} # this is element belongs to object self
        for s in dictionary:
            abbr = self.toAbbr(s)
            words = self.abbrDict[abbr] if abbr in self.abbrDict else set()
            words.add(s)
            abbrDict[abbr] = words
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.toAbbr(word)
        words = self.abbrDict.get(abbr, None)
        return words is None or len(words) == 1 and word in words
        
    def toAbbr(self, s):
        n = len(s)
        if n <= 2:
            return s
        return s[0] + str(n-2) + s[n-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")