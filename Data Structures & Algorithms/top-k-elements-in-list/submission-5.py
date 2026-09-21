class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for i in nums : 
            myMap[i] = myMap.get(i,0) + 1
        arr = [(-count,num) for num,count in myMap.items()]
        heapq.heapify(arr)
        result = []

        for _ in range (k) : 
            count,num = heapq.heapop(arr)
            result.append(num)
        return result
