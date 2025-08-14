from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)           # count all chars
        for i, ch in enumerate(s):  # first index with count == 1
            if freq[ch] == 1:
                return i
        return -1
