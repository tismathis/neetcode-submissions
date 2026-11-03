class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1) Intervalles entièrement AVANT newInterval (ils finissent avant qu'il commence)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2) Intervalles qui CHEVAUCHENT newInterval : on fusionne
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # 3) Intervalles entièrement APRÈS : on les ajoute tels quels
        while i < n:
            result.append(intervals[i])
            i += 1

        return result