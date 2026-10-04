class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # prochaine racine à lire dans preorder

        def build(left, right):
            # Plage vide dans inorder : pas de sous-arbre
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = pos[root_val]
            root.left = build(left, mid - 1)    # construit d'abord la gauche
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)