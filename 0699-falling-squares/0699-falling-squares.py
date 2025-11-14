class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        heights = [0] * n
        
        for i in range(n):
            left_i, size_i = positions[i]
            right_i = left_i + size_i
            heights[i] += size_i
            
            for j in range(i + 1, n):
                left_j, size_j = positions[j]
                right_j = left_j + size_j
                
                if left_j < right_i and left_i < right_j:
                    heights[j] = max(heights[j], heights[i])
        
        result = []
        current_max = 0
        for height in heights:
            current_max = max(current_max, height)
            result.append(current_max)
        
        return result