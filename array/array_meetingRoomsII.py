__author__ = 'yusizhang'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # https://leetcode.com/discuss/82292/explanation-super-easy-java-solution-beats-from-@pinkfloyda

        if not intervals or len(intervals) == 0:
            return 0
        if len(intervals) == 0:
            return 1

        meeting_start_time = [None] * len(intervals)
        meeting_end_time = [None] * len(intervals)
        current_end_time_index = 0
        for i in range(len(intervals)):
            meeting_start_time[i] = intervals[i].start
            meeting_end_time[i] = intervals[i].end
        meeting_start_time.sort()
        meeting_end_time.sort()
        rooms = 0
        for i in range(len(intervals)):
            # only need to compare the current meeting start time with the current meeting end time.
            if meeting_start_time[i] < meeting_end_time[current_end_time_index]:
                rooms += 1
            else:
                #the last meeting in the previous room is over, then we can use that room. So no need to increate rooms
                current_end_time_index += 1
        return rooms

