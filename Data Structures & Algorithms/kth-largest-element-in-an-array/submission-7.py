import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)          # O(n)

        for _ in range(k - 1):          # remove the k-1 largest
            heapq.heappop(maxHeap)

        return -maxHeap[0]              # the top is now the k-th largest