class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        result = []
        for char in baseStr:
            result.append(find(char))
        
        return ''.join(result)