class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"
        hex_digits = []

        # Extract 8 hex digits (32 bits)
        for _ in range(8):
            hex_digits.append(chars[num & 0xF])
            num >>= 4  # preserves sign bit if num is negative

        # Convert to string, reverse for correct order
        res = ''.join(reversed(hex_digits)).lstrip('0')
        return res or "0"
