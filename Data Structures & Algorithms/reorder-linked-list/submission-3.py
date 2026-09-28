# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        finalList = ListNode() 
        curr = head 
        i = 0 
        while curr :
            i +=1
            curr = curr.next
        newTab = [ i for i in range(i)] 
        l = 0 
        r = len(newTab) -1 
        while l < r :
            finalList.next = newTab[l]
            finalList.next = newTab[r]
            l +=1
            r -=1 
        return finalList 

         

