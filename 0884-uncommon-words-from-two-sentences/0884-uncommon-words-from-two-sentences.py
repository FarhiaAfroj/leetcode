class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        words = s1.split() + s2.split()
        count = Counter(words)

        return [word for word in count if count[word] == 1]