class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        
        freq = list(Counter(word).values())
        freq.sort(reverse=True)
        min_deletions = float('inf')
        
        for i in range(len(freq)):
            target_min = freq[i]
            target_max = target_min + k
            deletions = 0
            
            for f in freq:
                if f < target_min:
                    deletions += f
                elif f > target_max:
                    deletions += (f - target_max)
            
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions
        