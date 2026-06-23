"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda obj: obj.start)

        i = 0
        for j in range(1, len(intervals)):
            if intervals[j].start < intervals[i].end:
                return False
            i += 1
        return True


        '''
                for j in range(1, len(intervals)):
            if intervals[j].start < intervals[i].start:
                temp = intervals[i]
                intervals[i] = intervals[j]
                intervals[j] = temp
                i += 1 '''