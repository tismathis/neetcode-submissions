class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = []

        for point in points : 
            distance = (((point[0])^2 + (point[1])^2))^1/2
            heapq.heappush(heap,[distance,point]) 
        
        return [heap[i][1] for i in range(-1,k,-1)]

