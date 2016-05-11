__author__ = 'yusizhang'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    """
    Given a collection of intervals, merge all overlapping intervals.

    For example,
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].
    """
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # step 1. sort intervals based on the start value
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        # step2. loop each interval to insert to result set or generate new interval
        for interval in intervals:
            if len(intervals) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                # Has overlap, modify the last interval's end in the result set.
                # No need to worry about the start, since it is sorted already
                result[-1].end = max(interval.end, result[-1].end)
        return result