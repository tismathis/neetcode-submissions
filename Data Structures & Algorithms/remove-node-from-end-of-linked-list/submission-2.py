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
        

        while ((length-n) != 0 ):
            prev = curr 
            curr = curr.next 
            n -=1
        prev = curr.next 
        return prev

        