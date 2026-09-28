# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        duplicates = set()
        curr = head
        index = 0 
        
        while curr : 
            if index not in duplicates :
                duplicates.add(index)
                index +=1
            else :
                return False 
            curr = curr.next
        return True

