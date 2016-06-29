class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
        return stack.pop()
        
        """
        def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

        def evalRPN(self, tokens):
            if not tokens:
                return 0
    
            stack = []
    
            for token in tokens:
                if token in self.operators:
                    stack.append(self.operators[token](stack.pop(), stack.pop()))
                else:
                    stack.append(int(token))
    
            return stack[0]
        """
        