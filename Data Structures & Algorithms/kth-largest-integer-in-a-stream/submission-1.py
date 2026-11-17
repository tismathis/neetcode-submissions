class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-k]
        for num in nums : 
            heap.heappush(heap,-num) 
        return heap

    def add(self, val: int) -> int:
        heappush(self.heap,-val)
        return -heapq.heappop(heap)
        
