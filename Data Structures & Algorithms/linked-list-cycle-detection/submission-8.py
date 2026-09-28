# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        duplicates = set()
        curr = head
        
        while curr : 
            if curr.val not in duplicates :
                duplicates.add(curr.val)
            else :
                return False 
            curr = curr.next
        return True

