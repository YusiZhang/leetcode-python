class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pPointer = sPointer = ss = 0
        start = -1
        while sPointer < len(s):
            if pPointer < len(p) and (s[sPointer] == p[pPointer] or p[pPointer] == '?'):
                sPointer += 1
                pPointer += 1
                continue
            if pPointer < len(p) and p[pPointer] == "*":
                start = pPointer
                pPointer += 1
                ss = sPointer
                continue
            if start != -1:
                pPointer = start + 1
                ss += 1
                sPointer = ss
                continue
            return False

        while pPointer < len(p) and p[pPointer] == "*":
            pPointer += 1
        if pPointer == len(p):
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    s = "aaabc"
    p = "a*b*c"
    print solution.isMatch(s, p)