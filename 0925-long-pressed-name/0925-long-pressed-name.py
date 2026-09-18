class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for ch in typed:
            if i < len(name) and name[i] == ch:
                i += 1
            elif i == 0 or ch != name[i - 1]:
                return False

        return i == len(name)