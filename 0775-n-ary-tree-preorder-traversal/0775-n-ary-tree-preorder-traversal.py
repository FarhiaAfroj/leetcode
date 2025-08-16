class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            for child in reversed(node.children):
                stack.append(child)
        return result
