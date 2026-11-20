from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = []
        for x, y in points:
            heap.append((x * x + y * y, x, y))
        heapq.heapify(heap)  # O(n), faster than n pushes

        return [[x,y] for _,x,y  in (heapq.heappop(heap) for _ in range(k))]

