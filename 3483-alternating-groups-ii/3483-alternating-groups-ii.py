class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        """
        :param colors: List[int] of length n (0 = red, 1 = blue), treated as a circle
        :param k: int >= 3
        :return: int number of alternating groups of length k
        """
        n = len(colors)
        ans = 0
        cnt = 0

        # Slide over the circle twice to handle wrap‑around naturally
        for i in range(2 * n):
            cur = colors[i % n]
            prev = colors[(i - 1) % n] if i > 0 else None
            if i > 0 and cur == prev:
                cnt = 1
            else:
                cnt += 1

            # Only count groups that fully occur in the second half (i >= n),
            # and only when current alternating run is at least k tiles long.
            if i >= n and cnt >= k:
                ans += 1

        return ans


        