# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root : 
            return []
        
        q = deque() 
        array = []

        for i in range(len(q)) :
            curr = q.popleft()
            array.append([curr])
            if curr.left :
                q.append(curr.left)
            if curr.right :
                q.append(cur.right)
                
        return array 

