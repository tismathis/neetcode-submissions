# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        testArray = []
        index = 0

        for k in lists : 
            curr = k 
            while curr :
                testArray.append(curr.val)
                curr = curr.next
                index +=1
        
        testArray.sort()
        newList = ListNode() 
        for i in testArray :
            newList = ListNode(i)
            newList = newList.next
        return newList.next




