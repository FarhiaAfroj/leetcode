class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            if data[i] < 128:
                i += 1
            elif 192 <= data[i] <= 223:
                if i + 1 >= n or not (128 <= data[i+1] <= 191):
                    return False
                i += 2
            elif 224 <= data[i] <= 239:
                if i + 2 >= n or not (128 <= data[i+1] <= 191) or not (128 <= data[i+2] <= 191):
                    return False
                i += 3
            elif 240 <= data[i] <= 247:
                if i + 3 >= n or not (128 <= data[i+1] <= 191) or not (128 <= data[i+2] <= 191) or not (128 <= data[i+3] <= 191):
                    return False
                i += 4
            else:
                return False
        return True