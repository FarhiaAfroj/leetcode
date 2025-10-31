class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1, 2]
        for i in range(2, 32):
            fib.append(fib[i-1] + fib[i-2])
        
        s = bin(n)[2:]
        length = len(s)
        res = 0
        prev_bit = 0
        
        for i in range(length):
            if s[i] == '1':
                res += fib[length - i - 1]
                if prev_bit == 1:
                    return res
                prev_bit = 1
            else:
                prev_bit = 0
        
        return res + 1