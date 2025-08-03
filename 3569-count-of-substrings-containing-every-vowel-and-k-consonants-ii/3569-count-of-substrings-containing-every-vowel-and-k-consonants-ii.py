class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        VOWELS = "aeiou"

        def at_most(max_k: int) -> int:
            if max_k < 0:
                return 0
            res = 0
            total_vowels = 0
            distinct = 0
            # প্রতিটি ভাওয়েলের সর্বশেষ ইনডেক্স ট্র্যাক
            last = {v: -1 for v in VOWELS}
            left = 0

            for right, c in enumerate(word):
                if c in VOWELS:
                    total_vowels += 1
                    if last[c] < left:
                        distinct += 1
                    last[c] = right

                # shrinking এর সময় consonant_count ≤ max_k রাখতে হবে
                while (right - left + 1) - total_vowels > max_k:
                    if word[left] in VOWELS and last[word[left]] == left:
                        distinct -= 1
                    if word[left] in VOWELS:
                        total_vowels -= 1
                    left += 1

                if distinct == 5:
                    earliest = min(last[v] for v in VOWELS)
                    res += earliest - left + 1

            return res

        return at_most(k) - at_most(k - 1)

        