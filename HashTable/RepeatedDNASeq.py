class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashset = set()
        dna = set()
        for i in range(9, len(s)):
        	substring = s[i-9:i+1]
        	hashcode = self.encode(substring)
        	if hashcode in hashset:
        		dna.add(substring)
        	else:
        		hashset.add(hashcode)
        return list(dna)
    def encode(self, s):
    	sum = 0
    	for c in s:
    		if c == 'A':
    			sum = sum * 4
    		elif c == 'C':
    			sum = sum * 4 + 1
    		elif c == "G":
    			sum = sum * 4 + 2
    		else:
    			sum = sum * 4 + 3
    	return sum