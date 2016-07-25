class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        a=strs[0]
        for i in xrange(1,len(strs)):
            l=len(a)
            while strs[i][:l]!=a[:l]:
                l-=1
            a=strs[i][:l] # current common prefix
        return a