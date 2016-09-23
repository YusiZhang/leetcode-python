import re
import operator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # http://bookshadow.com/weblog/2015/06/23/leetcode-basic-calculator-ii/
        # revisit 弄清楚正则表达式
        s = re.sub(r'\d+', ' \g<0> ', s)
        # ' \g<0> '表示替代原来group 0的match,为match加上前后空格. 否则“0+0" 这种无法被split
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        expression = s.split()
        total = d = idx = 0
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)