import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_count = 1
        for i in range(n):
            slope_count = defaultdict(int)
            x1, y1 = points[i]
            same_point = 0
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same_point += 1
                    continue
                g = math.gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g
                slope_count[(dx, dy)] += 1
            
            current_max = 0
            for count in slope_count.values():
                if count > current_max:
                    current_max = count
            current_max += same_point + 1  
            if current_max > max_count:
                max_count = current_max
        
        return max_count