class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"
        hex_digits = []

        
        for _ in range(8):
            hex_digits.append(chars[num & 0xF])
            num >>= 4  

        res = ''.join(reversed(hex_digits)).lstrip('0')
        return res or "0"
