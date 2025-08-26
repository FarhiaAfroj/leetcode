from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Build the graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            queue = deque([(start, 1.0)])
            visited = set()
            visited.add(start)
            while queue:
                node, current_product = queue.popleft()
                if node == end:
                    return current_product
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_product * weight))
            return -1.0
        
        results = []
        for query in queries:
            results.append(bfs(query[0], query[1]))
        return results