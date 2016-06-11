class Solution(obcountect):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ''' 
	    O(nm)
	    n, m, k = len(s), len(words[0]), len(words)
	    暴力做法，枚举开始位置，判断之后长度m*k的子串是否由给定字符串集合组成，最坏复杂度为O(nmk)。
	    对于长度为m的字符串，0与m位置开始的区别，只在于少了s[0:m]，多了s[m*k+1:(m+1)*k]，所以产生了许多
	    冗余操作。我们根据开始位置0~m-1分类，扫描字符串s，使用一个滑动窗口记录当前匹配了那些字符串，当下一个
	    字符串不在words中，清空窗口(任意包含该串的均不合法)，如果记录的出现次数超过了words中数量，表示需要滑动窗口，
	    窗口中单词数量等于k时，更新答案。
	    '''
        words_dict = {}
        wordNums = len(words)
        for word in words:
        	words_dict[word] = words_dict.get(word, 0) + 1
        wordLen = len(words[0])
        result = []
        for i in range(len(s)+1 - wordLen*wordNums):
        	curr = {}
        	count = 0
        	while count < wordNums:
        		word = s[i+count*wordLen: i+count*wordLen+wordLen]
        		if word not in words_dict:
        			break
        		curr[word] = curr.get(word, 0) + 1
        		if curr[word] > words_dict[word]:
        			break
        		count += 1
        	if count == wordNums:
        		result.append(i)

        return result
