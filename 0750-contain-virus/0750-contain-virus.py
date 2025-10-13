class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0
        
        while True:
            regions = []
            frontiers = []
            perimeters = []
            visited = [[False] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region = []
                        frontier = set()
                        perimeter = 0
                        stack = [(i, j)]
                        visited[i][j] = True
                        
                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))
                            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                                nx, ny = x+dx, y+dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        perimeter += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))
                        
                        regions.append(region)
                        frontiers.append(frontier)
                        perimeters.append(perimeter)
            
            if not regions:
                break
            
            max_idx = 0
            max_frontier = 0
            for i, frontier in enumerate(frontiers):
                if len(frontier) > max_frontier:
                    max_frontier = len(frontier)
                    max_idx = i
            
            walls += perimeters[max_idx]
            
            for i, region in enumerate(regions):
                if i == max_idx:
                    for x, y in region:
                        isInfected[x][y] = -1
                else:
                    for x, y in region:
                        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 0:
                                isInfected[nx][ny] = 1
        
        return walls