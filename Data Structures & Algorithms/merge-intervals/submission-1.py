class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        newlist = [] 

        intervals.sort(key = lambda i: i[0]) #tab is now sorted !! 

        newlist.append(intervals[0])

        for i in range(1,len(intervals)) : 

            if newlist[-1][1] >= intervals[i][0] : 

                newlist[-1] = [min(newlist[-1][0],intervals[i][0]),max(newlist[-1][1],intervals[i][1])] #we add to the temp list the merge 
            else : 
                newlist.append(intervals[i])
        return newlist 
            


