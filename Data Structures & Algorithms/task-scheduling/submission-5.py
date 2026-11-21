class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        heap = [-f for f in freq if f > 0]
        heapq.heapify(heap)

        time = 0
        while heap:
            temp = []
            count = 0
            for _ in range(n + 1):
                if heap:
                    pop = heapq.heappop(heap) + 1
                    count += 1
                    if pop != 0:
                        temp.append(pop)
            for item in temp:
                heapq.heappush(heap, item)

            time += (n + 1) if heap else count
        return time