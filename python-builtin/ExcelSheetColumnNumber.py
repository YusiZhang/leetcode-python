"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y : x * 26 + y, [ord(c) - ord("A") + 1 for c in list(s)])
        # http://www.python-course.eu/lambda.php