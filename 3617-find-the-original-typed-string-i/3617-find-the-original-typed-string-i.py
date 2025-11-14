class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        
        result = 1
        for length in groups:
            if length > 1:
                result += (length - 1)
        return result