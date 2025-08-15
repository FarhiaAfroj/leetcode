import math

class Solution:
    def constructRectangle(self, area: int):
    
        for w in range(int(math.sqrt(area)), 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]
