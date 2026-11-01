"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
    
        start = intervals.sort(key = lambda i : i.start)
        end = intervals.sort(key = lambda i : i.end)

        i,j = 1,0 

        counter = 1 

        while i < len(intervals) : 

            if start[i] < end[j] : 
                counter +=1 
                i+=1
            j +=1 

        return counter 