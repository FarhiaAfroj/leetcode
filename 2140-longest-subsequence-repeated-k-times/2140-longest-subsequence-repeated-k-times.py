class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter, deque
        
        freq = Counter(s)
        chars = sorted([c for c in set(s) if freq[c] >= k], reverse=True)
        
        ans = ""
        queue = deque([""])
        
        while queue:
            curr = queue.popleft()
            for c in chars:
                new_seq = curr + c
                if self.isSubsequence(s, new_seq * k):
                    if len(new_seq) > len(ans) or (len(new_seq) == len(ans) and new_seq > ans):
                        ans = new_seq
                    queue.append(new_seq)
        return ans
    
    def isSubsequence(self, s: str, pattern: str) -> bool:
        i = 0
        for char in s:
            if i < len(pattern) and char == pattern[i]:
                i += 1
        return i == len(pattern)