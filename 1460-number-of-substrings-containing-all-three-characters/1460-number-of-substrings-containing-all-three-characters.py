class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        ans = 0
        left = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            # As long as window has all three, it’s “valid”
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right
                count[s[left]] -= 1
                left += 1

        return ans

        