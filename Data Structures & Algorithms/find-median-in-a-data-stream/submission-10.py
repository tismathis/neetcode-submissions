class MedianFinder:

    def __init__(self):
        self.currList = []

    def addNum(self, num: int) -> None:
        self.currList.append(num)

    def findMedian(self) -> float:
        if not self.currList:
            return 0
        nums = sorted(self.currList)
        m = len(nums) // 2

        if len(nums) % 2 == 0:
            return (nums[m - 1] + nums[m]) / 2
        else:
            return nums[m]