class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter

        words = re.findall(r"[a-zA-Z]+", paragraph.lower())
        banned = set(banned)

        count = Counter(word for word in words if word not in banned)

        return count.most_common(1)[0][0]