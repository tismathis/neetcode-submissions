# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]

        while stack: 
            pleft , qright = stack.pop()

            if pleft.left != qright.left  :
                return False 
            if pleft.right != qright.right :
                return False 
            else :
                stack.append((pleft.left,pleft.right))
                satck.append((qright.left,qright.right))
        return True

            


