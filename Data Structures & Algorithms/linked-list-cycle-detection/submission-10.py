class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if curr in seen:      # been at this exact node before
                return True
            seen.add(curr)
            curr = curr.next
        return False              # reached the end, so no cycle