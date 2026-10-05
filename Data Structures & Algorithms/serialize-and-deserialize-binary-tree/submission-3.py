
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        out = []
        while q:
            curr = q.popleft()
            if curr is None:
                out.append("#")
                continue
            out.append(str(curr.val))
            q.append(curr.left)
            q.append(curr.right)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if vals[i] != "#":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if vals[i] != "#":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i += 1
        return root