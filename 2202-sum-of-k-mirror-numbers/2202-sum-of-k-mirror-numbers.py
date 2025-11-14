class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_mirror(num, base):
            digits = []
            temp = num
            while temp > 0:
                digits.append(temp % base)
                temp //= base
            return digits == digits[::-1]
        
        result = []
        count = 0
        length = 1
        
        while count < n:
            if length == 1:
                for i in range(1, 10):
                    if is_mirror(i, k):
                        result.append(i)
                        count += 1
                        if count == n:
                            break
            else:
                half_len = (length + 1) // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                
                for num in range(start, end):
                    s = str(num)
                    if length % 2 == 0:
                        palindrome = int(s + s[::-1])
                    else:
                        palindrome = int(s[:-1] + s[::-1])
                    
                    if is_mirror(palindrome, k):
                        result.append(palindrome)
                        count += 1
                        if count == n:
                            break
            
            length += 1
        
        return sum(result)