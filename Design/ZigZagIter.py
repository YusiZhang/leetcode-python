class ZigZagIter(object):
    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        length, myIter = self.data.pop(0)
        # pop out each of first element in the iter.
        # [1,2,3] [4,5,6,7] -> next(v1): 1, next(v2):4, next(v1):2, next(v2): 5 ...
        if length > 1:
            self.data.append((length - 1, myIter))
        return next(myIter)

    def hasNext(self):
        return bool(self.data)

if __name__ == '__main__':

    v1 = [1, 2, 3]
    v2 = [4, 5, 6, 7]

    i, v = ZigZagIter(v1, v2), []
    while i.hasNext():
        v.append(i.next())

    print v
