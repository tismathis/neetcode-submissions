class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-k]
        for num in nums : 
            heapq.heappush(heap,-num) 
        return heap

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        return -heapq.heappop(heap)
        
