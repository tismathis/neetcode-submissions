# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev,curr = None,head

        length = 0 

        fast = head 
        while fast :
            fast = fast.next 
            length +=1
        
        complem = length-n +1 
        while (complem!= 0 ):
            prev = curr 
            curr = curr.next 
            complem -=1
            prev.next = curr.next 
        return prev

        if complem == 0:
            return head.next
        return prev

        