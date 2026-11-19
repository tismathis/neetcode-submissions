import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 == stone2:
                continue

            heapq.heappush(heap, -(stone1 - stone2))

        return -heap[0] if heap else 0