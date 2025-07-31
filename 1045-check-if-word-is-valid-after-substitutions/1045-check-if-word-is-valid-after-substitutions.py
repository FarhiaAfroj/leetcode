class Solution:
    def isValid(self, s):
        if len(s) % 3 != 0:
            return False
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop(); stack.pop(); stack.pop()
        return not stack
