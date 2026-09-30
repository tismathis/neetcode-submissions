class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        length = 0
        fast = head
        while fast:
            fast = fast.next
            length += 1

        complem = length - n
        if complem == 0:          # removing the head
            return head.next

        while complem != 0:
            prev = curr
            curr = curr.next
            complem -= 1

        prev.next = curr.next     # unlink once, after the loop
        return head