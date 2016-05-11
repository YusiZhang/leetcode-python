__author__ = 'yusizhang'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals or len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals = sorted(intervals, key=lambda x:x.start)

        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if prev_interval.end > intervals[i].start:
                return False
            else:
                prev_interval = intervals[i]
        return True