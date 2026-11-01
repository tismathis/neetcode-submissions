"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 1 :
            return 1 

        counter = 0

        intervals.sort(key = lambda i : i.start) 

        for i in range(1,len(intervals)) : 
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start : 

                counter +=1 
        return counter 


        

        