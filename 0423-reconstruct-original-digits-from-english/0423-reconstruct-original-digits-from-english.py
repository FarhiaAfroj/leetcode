from collections import defaultdict

class Solution:
    def originalDigits(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
            
        digit_count = [0] * 10
        
        # Zero: 'z' is unique
        digit_count[0] = count['z']
        count['e'] -= digit_count[0]
        count['r'] -= digit_count[0]
        count['o'] -= digit_count[0]
        
        
        digit_count[2] = count['w']
        count['t'] -= digit_count[2]
        count['o'] -= digit_count[2]
        
        
        digit_count[4] = count['u']
        count['f'] -= digit_count[4]
        count['o'] -= digit_count[4]
        count['r'] -= digit_count[4]
        
        
        digit_count[6] = count['x']
        count['s'] -= digit_count[6]
        count['i'] -= digit_count[6]
        
       
        digit_count[8] = count['g']
        count['e'] -= digit_count[8]
        count['i'] -= digit_count[8]
        count['h'] -= digit_count[8]
        count['t'] -= digit_count[8]
        
        
        digit_count[3] = count['h']
        count['t'] -= digit_count[3]
        count['r'] -= digit_count[3]
        count['e'] -= 2 * digit_count[3]
        
        
        digit_count[5] = count['f']
        count['i'] -= digit_count[5]
        count['v'] -= digit_count[5]
        count['e'] -= digit_count[5]
        
        
        digit_count[7] = count['s']
        count['e'] -= 2 * digit_count[7]
        count['v'] -= digit_count[7]
        count['n'] -= digit_count[7]
        
        
        digit_count[1] = count['o']
        count['n'] -= digit_count[1]
        count['e'] -= digit_count[1]
        
        
        digit_count[9] = count['i']
        count['n'] -= 2 * digit_count[9]
        count['e'] -= digit_count[9]
        
        result = ''
        for i in range(10):
            result += str(i) * digit_count[i]
        return result