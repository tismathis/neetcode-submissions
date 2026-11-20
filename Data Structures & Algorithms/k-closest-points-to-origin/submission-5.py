class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points :
            d = -(x*x,y*y) 
            if len(heap) < k : 
                heapq.heappush(heap,(d,x,y))
            elif d > heap[0][0] : 
                heapq.heapreplace(heap,(d,x,y)) #closer than the farthest one kept so far 
        return [[x,y] for _,x,y in heap] 