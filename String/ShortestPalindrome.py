class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # https://github.com/IDeserve/learn/blob/master/ShortestPalindrome.java
        # https://www.youtube.com/watch?v=c4akpqTwE5g
        # http://blog.csdn.net/xudli/article/details/45931667
        # http://blog.csdn.net/v_july_v/article/details/7041827
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

if __name__ == '__main__':
    solution = Solution()
    s = "aacecaaa"
    print solution.shortestPalindrome(s)