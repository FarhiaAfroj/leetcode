import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        total = 0
        for rect in rects:
            a, b, x, y = rect
            area = (x - a + 1) * (y - b + 1)
            total += area
            self.areas.append(total)

    def pick(self) -> List[int]:
        rand = random.randint(1, self.areas[-1])
        idx = 0
        for i, area in enumerate(self.areas):
            if rand <= area:
                idx = i
                break
        
        a, b, x, y = self.rects[idx]
        if idx > 0:
            rand -= self.areas[idx - 1]
        
        width = x - a + 1
        row = (rand - 1) // width
        col = (rand - 1) % width
        return [a + col, b + row]