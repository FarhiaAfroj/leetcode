import unicodedata

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = unicodedata.normalize('NFC', s.lower())
        t = unicodedata.normalize('NFC', t.lower())
        return Counter(s) == Counter(t)
