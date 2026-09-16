class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd

        counts = Counter(deck).values()
        x = 0

        for count in counts:
            x = gcd(x, count)

        return x >= 2