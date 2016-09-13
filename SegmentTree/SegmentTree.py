class SegmentTreeNode(object):
    def __init__(self, start, end, value):
        """

        :param start:
        :type start: int
        :param end:
        :type end: int
        :param value:
        """
        self.start = start
        self.end   = end
        self.value = value
        self.left = self.right = None


class SegmentTree(object):
    # def __init__(self, start, end, input_list):
    #     self.root = self.build(start, end, input_list)

    def build(self, start, end, input_list):
        if start > end:
            return None

        root = SegmentTreeNode(start, end, 0)

        if start != end:
            mid = (start + end) / 2
            root.left = self.build(start, mid, input_list)
            root.right = self.build(mid+1, end, input_list)
            root.value = root.left.value + root.right.value  # this segment tree is used to query range sum
        else:
            root.value = input_list[start]

        return root

    def querySegmentTree(self, root, start, end):
        """

        :param root:
        :type root: SegmentTreeNode
        :param start:
        :param end:
        :return:
        """
        # total overlap
        if start == root.start and end == root.end:
            return root.value

        mid        = (root.start + root.end) / 2
        leftValue  = 0
        rightValue = 0

        # partial overlap, and some fall into left child section
        if start <= mid:
            if mid < end:
                # partial value comes from left child section
                leftValue = self.querySegmentTree(root.left, start, mid)
            else:
                # total overlap, result comes from left child section
                leftValue = self.querySegmentTree(root.left, start, end)

        # partial overlap, and some fall into right child section
        if mid < end:
            if start <= mid:
                # partial value comes from right child section
                rightValue = self.querySegmentTree(root.right, mid+1, end)
            else:
                # total overlap, result comes from right child section
                rightValue = self.querySegmentTree(root.right, start, end)

        # else: no overlap at all
        # this is for getting range sum
        return leftValue + rightValue

    def modifySegmentTree(self, root, index, value):
        """
        :type root: SegmentTreeNode
        :type index: int
        """
        if root.start == index and root.end == index:
            # todo has to be add on, cannot update?
            # root.value += value
            root.value = value
            return

        mid = (root.start + root.end) / 2
        if root.start <= index and index <= mid:
            self.modifySegmentTree(root.left, index, value)

        if mid < index and index <= root.end:
            self.modifySegmentTree(root.right, index, value)

        # this is for range sum, change it to min/max func when you need range min/max
        root.value = root.left.value + root.right.value
        return

if __name__ == '__main__':
    myList = [1,-1,2,3,0]
    segmentTree = SegmentTree()
    root = segmentTree.build(0, 4, myList)
    sumAll = segmentTree.querySegmentTree(root, 0, 4)
    print sumAll

    print segmentTree.querySegmentTree(root, 0, 2)

    segmentTree.modifySegmentTree(root, 1, 0)
    print segmentTree.querySegmentTree(root, 0, 2)




