"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length <= 1:
            return length
        max_count = 1
        for index1 in range(length):
            p1 = points[index1]
            gradients = {}
            infinite_count = 1      #!!!!!
            duplicate_count = 0
            for index2 in range(index1+1, length):
                p2 = points[index2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if 0 == dx and 0 == dy:
                    duplicate_count += 1
                if 0 == dx:
                    infinite_count += 1
                else:
                    g = float(dy) / dx
                    gradients[g] = gradients[g] + 1 if gradients.has_key(g) else 2      #!!!!
            if infinite_count > max_count:
                max_count = infinite_count
            for k, v in gradients.items():
                v += duplicate_count
                if v > max_count:
                    max_count = v
        return max_count