"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, ints: List[Interval]) -> int:
        times = []
        for i in ints:
            times.append((i.start, 1))
            times.append((i.end, -1))
    
        times.sort(key=lambda x: (x[0], x[1]))
        res = 0
        curr = 0
        for t in times:
            curr += t[1]
            res = max(res, curr)
        return res