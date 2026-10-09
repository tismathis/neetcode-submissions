class MedianFinder:

    def __init__(self):
        self.currList = [] 
        

    def addNum(self, num: int) -> None:
        self.currList.append(num) 
        

    def findMedian(self) -> float:
        if not self.currList : 
            return 0
        self.currList = self.currList.sort()
        m = len(self.currList)//2

        if len(self.currList) % 2 == 0:
            meanOfMiddle = (currList[m-1] + currList[m])/2
            return meanOfMiddle
        else : 
            return currList[m] 
            

        
        