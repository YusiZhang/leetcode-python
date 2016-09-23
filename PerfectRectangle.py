import collections


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l,b), (r,b), (r, t), (l, t)
            for p, q in zip((A,B,C,D), (1,2,4,8)):
                # 同一个点不能作为左上左下右上右下两次,否则违规
                if points[p] & q:
                    return False
                points[p] |= q
        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3,6,9,12,15):
                    return False

        return True

"""
        G
D |-----|-----| C
  |     |     |
H |-----I-----| F
  |     |     |
A |-----|-----| B
        E

points[E] = points[A] | points[B] = 3 （左下顶点、右下顶点的并）
points[F] = points[B] | points[C] = 6 （右下顶点、右上顶点的并）
points[G] = points[C] | points[D] = 12 （右上顶点、左上顶点的并）
points[H] = points[A] | points[D] = 9 （左下顶点、左上顶点的并）
points[I] = points[A] | points[B] | points[C] | points[D] = 15（四个顶点的并）
"""