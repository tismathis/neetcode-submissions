class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        


        

        for i in range(len(intervals)) : 
            if intervals[i][1] > newInterval[0] : 
                if newInterval[1] < intervals[i+1][0] :
                    List.concat(intervals[i][1],newInterval,intervals[i+1])
                
                else : 
                    List.concat(intervals[i][1],newInterval)
            else : 
                if newInterval[0] > intervals[i][1] : 
                    intervals.append(newInterval,i+1)
                    
        return intervals 
