class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for i in nums : 
            if i in myMap :
                myMap[i] +=1
            myMap[i] = 1
        arr = myMap.values()
        heapq.heapify(arr)
        j = 0
        while j < k:
            arrFin = list(heapq.heappop(arr))
            k+=1
        return arrFin