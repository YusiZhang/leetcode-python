class Vector2D(object):

    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.vec = vec2d

    def next(self):
        self.hasNext()
        val = self.vec[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self):
        while self.row < len(self.vec):
            while self.col < len(self.vec[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False


        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())