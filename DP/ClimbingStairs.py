class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        step_one = 1
        step_two = 1
        result = 0
        for i in xrange(2, n+1):
            result = step_one + step_two
            step_two = step_one
            step_one = result
        return result