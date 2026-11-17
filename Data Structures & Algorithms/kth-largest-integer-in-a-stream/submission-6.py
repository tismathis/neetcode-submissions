class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-k]
        for num in nums : 
            heapq.heappush(heap,-num) 
        

    def add(self, val: int) -> int:
        heapq.heappush(heapq,-val)
        return -heapq.heappop(heap)
        
