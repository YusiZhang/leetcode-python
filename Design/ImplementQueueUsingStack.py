class Queue(object):
    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        self.move()
        self.outStack.pop()

    def peek(self):
        self.move()
        return self.outStack[-1]

    def empty(self):
        return (not self.inStack) and (not self.outStack) 

    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())



