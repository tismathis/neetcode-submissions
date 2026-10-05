# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

            if root :
                return ""
            q = deque([root])
            out = []
            while q :
                curr =q.popleft()
                if curr.val == None :
                    out.append("#")
                    continue
                out.append(str(curr.val))
                q.append(curr.left) 
                q.append(curr.right)
            return ",".join(out)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data :
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 0

        while deque :
            curr = q.popleft()
            if vals[i] != "#" :
                 node.left = TreeNode(int(vals[i]))
                 q.append(curr.left)
            i +=1
            if vals[i] !="#":
                node.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i+=1
        return root 







