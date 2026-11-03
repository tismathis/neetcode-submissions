class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                # intervals[i] est entièrement avant newInterval : on le garde
                result.append(intervals[i])

            elif newInterval[1] < intervals[i][0]:
                # intervals[i] est entièrement après : on place newInterval ici,
                # puis tout le reste sans changement
                result.append(newInterval)
                return result + intervals[i:]

            else:
                # ils se chevauchent : on fusionne dans newInterval
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]

        # newInterval va à la fin (aucun intervalle n'était après lui)
        result.append(newInterval)
        return result