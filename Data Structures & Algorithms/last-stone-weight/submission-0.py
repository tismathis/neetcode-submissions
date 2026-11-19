class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones :
            heapq.heappush(heap,stone)

        while len(heap) >= 1 :
            stone1 = heapq.heappop(heap)  
            stone2 = heapq.heappop(heap)

            if stone1 == stone2 : 
                continue 
            elif stone1 < stone2 :
                stone2 = stone2-stone1 
                heapq.heappush(heap,stone2) 
            else :
                stone1 = stone1-stone2 
                heapq.heappush(heap,stone1) 
        return heap[0]




        