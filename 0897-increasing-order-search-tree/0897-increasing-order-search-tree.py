class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        curr = dummy

        def inorder(node):
            nonlocal curr

            if not node:
                return

            inorder(node.left)

            curr.right = TreeNode(node.val)
            curr = curr.right

            inorder(node.right)

        inorder(root)

        return dummy.right