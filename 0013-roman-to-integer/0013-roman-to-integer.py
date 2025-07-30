class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev = 0
        # Traverse the string left to right
        for char in s:
            curr = roman[char]
            # If current is greater than previous, we subtract twice previous then add current
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total

# Example usage:
if __name__ == '__main__':
    test_cases = ["III", "LVIII", "MCMXCIV"]
    solution = Solution()
    for tc in test_cases:
        print("{} → {}".format(tc, solution.romanToInt(tc)))
