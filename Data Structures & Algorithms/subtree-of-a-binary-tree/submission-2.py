# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #first step is to find the root of subroot in themain tree. 
        stackMain = []
        stackSub = []
        stackMain[root] 
        stackSub[subRoot]

        while stack :
            curr = stack.pop()
            if curr != subRoot :
                stackMain.append(curr.left)
                stackMain.append(curr.right)
            else : 
                #We found the root of the subRoot in the Main Root 
                stackFinal = [(curr,subRoot)] 
                while stackFinal : 
                    a,b = stackFinal.pop()
                    if not a and not b : 
                        continue 
                    if not a or not b:
                        return False 
                    if a.val == b.val : 
                        stackFinal.append((a.left,b.left))
                        stackFinal.append((a.right,b.right))
                return True 






        