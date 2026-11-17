class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-k]
        for num in nums : 
            heapq.heappush(heap,-num) 
        

    def add(self, val: int) -> int:
        heapq.heappush(heap,-val)
        return -heapq.heappop(heap)
        
