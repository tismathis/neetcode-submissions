class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # 1. Go left as far as possible, saving nodes on the way
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. Visit the smallest node not yet visited
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # 3. Move to the right subtree
            curr = curr.right