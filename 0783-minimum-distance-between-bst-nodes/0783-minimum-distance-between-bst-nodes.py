class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        return min(vals[i] - vals[i - 1] for i in range(1, len(vals)))
        