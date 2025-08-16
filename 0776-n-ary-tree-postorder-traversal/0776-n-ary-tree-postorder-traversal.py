class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in node.children:
                stack.append(child)
        return ans[::-1]
