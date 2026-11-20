class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []

        visited = set()

        for num in nums : 
            if num in visited :
                continue 
            visited.add(num)
            heapq.heappush(maxHeap,-num) 

        return -maxHeap[k] 