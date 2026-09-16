class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(grid[i][j] > 0 for i in range(len(grid)) for j in range(len(grid)))
        front = sum(max(row) for row in grid)
        side = sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid)))

        return top + front + side