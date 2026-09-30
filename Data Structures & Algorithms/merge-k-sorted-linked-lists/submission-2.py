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
        dummy = ListNode()
        tail = dummy
        for v in testArray:
            tail.next = ListNode(v)   # attach
            tail = tail.next          # move forward
        return dummy.next




