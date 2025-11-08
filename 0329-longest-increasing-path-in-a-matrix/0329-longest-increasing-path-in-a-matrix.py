class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            
            max_path = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(x, y))
            
            memo[i][j] = max_path
            return max_path
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result