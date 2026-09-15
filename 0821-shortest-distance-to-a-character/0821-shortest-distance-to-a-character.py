class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        positions = [i for i in range(len(s)) if s[i] == c]

        for i in range(len(s)):
            result.append(min(abs(i - p) for p in positions))

        return result