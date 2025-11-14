class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        result = 0
        val = 0
        power = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                result += 1
            else:
               
                if val + power <= k:
                    val += power
                    result += 1
           
            if power <= k:  
                power <<= 1
        
        return result