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
            for _ in range(n + 1):
                if heap:
                    # pop, décrémenter, garder dans temp si != 0
                    pop = heapq.heappop(heap)
                    pop +=1
                    if pop != 0 : 
                        temp.append(pop)
            for item in temp:
                heapq.heappush(heap, item)

            # combien de temps ajouter pour ce cycle ?
            time += n
        return time