class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        i = 0 
        j = len(heights)-1
        

        while i < j :
            leftValue = heights[i]
            rightValue = heights[j]
            minValue = min(leftValue,rightValue) 
            distance = j-i
            finalValue = distance*minValue

            if finalValue > res :
                res = finalValue
            if min(heights[i+1],heights[j])*(distance-1) > finalValue:
                i+=1
            elif min(heights[i],heights[j-1])*(distance-1) > finalValue:
                j-=1
            else :
                i+=1
                j-=1
        return res 
            