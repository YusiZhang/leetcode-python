class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin)) #对于当前元素的最小值!!
        
        

    def pop(self):
        """
        :rtype: void
        """
        return self.q.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()