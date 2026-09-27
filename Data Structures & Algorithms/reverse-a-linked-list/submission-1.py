# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tab = []
        curr = head
        i = 0 
        while curr != null :
            tab[i] = curr
            curr = head.next
            i+=1
        
        newTab = [ListNode for i in range(len(tab),-1,-1)] 
        return newTab


    
    

        
        