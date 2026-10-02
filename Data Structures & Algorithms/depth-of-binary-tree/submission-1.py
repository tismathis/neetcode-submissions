# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0 
        curr = root 
        if curr.left or curr.right :
            return 1
        counter +=maxDepth(curr.left)
        counter +=maxDepth(curr.right)
