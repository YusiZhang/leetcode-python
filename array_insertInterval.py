__author__ = 'yusizhang'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    """
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

    You may assume that the intervals were initially sorted according to their start times.

    Example 1:
    Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

    Example 2:
    Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

    This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
    """
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        isInsert = False
        for interval in intervals:
            # has already inserted. this must come first
            if isInsert:
                result.append(interval)
                continue
            # current interval comes before the newInterval
            if interval.end < newInterval.start:
                result.append(interval)
                continue

            # the newIntercal comes before the current interval
            if interval.start > newInterval.end:
                result.append(newInterval)
                result.append(interval)
                isInsert = True
                continue

            # has overlap
            if interval.end >= newInterval.start and interval.start <= newInterval.end:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
                continue

        if not isInsert:
            result.append(newInterval)
        return result

if __name__ == '__main__':
    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(6,9))
    newInterval = Interval(2,5)

    for item in Solution().insert(intervals, newInterval):
        print str(item.start) + "  " + str(item.end)
