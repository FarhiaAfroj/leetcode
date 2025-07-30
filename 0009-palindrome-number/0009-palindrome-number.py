class Solution:
    def isPalindrome(self, x):
        # Negative numbers or numbers ending with 0 (and not zero) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        original = x

        # Revert half of the number
        while x > reverted:
            reverted = reverted * 10 + (x % 10)
            x //= 10

        # For odd number of digits, drop the middle digit
        return x == reverted or x == reverted // 10
