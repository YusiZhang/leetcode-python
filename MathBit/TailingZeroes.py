class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # think about how to know how many 5s are in a number n?
        # then think about how many 5s are in number n!
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
        
"""
public class Solution {
    public int trailingZeroes(int n) {
        int s = 0;
        while (n>4) s += (n/=5);
        return s;
    }
}
"""