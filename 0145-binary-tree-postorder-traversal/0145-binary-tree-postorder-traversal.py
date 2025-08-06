class Solution:
    def postorderTraversal(self, root):
        res = []
        # iterative stack-based implementation
        stack = []
        prev = None
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack[-1]
            if node.right and prev is not node.right:
                curr = node.right
            else:
                res.append(node.val)
                prev = stack.pop()
        return res

   