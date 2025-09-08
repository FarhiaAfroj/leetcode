class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def merge_sort_count(l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            count = merge_sort_count(l, mid) + merge_sort_count(mid+1, r)
            
           
            i = l
            j1 = mid+1
            j2 = mid+1
          
            low = l
            high = l
            for j in range(mid+1, r+1):
                while low <= mid and prefix[low] < prefix[j] - upper:
                    low += 1
                while high <= mid and prefix[high] <= prefix[j] - lower:
                    high += 1
                count += (high - low)
            
          
            sorted_arr = []
            i1 = l
            i2 = mid+1
            while i1 <= mid and i2 <= r:
                if prefix[i1] <= prefix[i2]:
                    sorted_arr.append(prefix[i1])
                    i1 += 1
                else:
                    sorted_arr.append(prefix[i2])
                    i2 += 1
            while i1 <= mid:
                sorted_arr.append(prefix[i1])
                i1 += 1
            while i2 <= r:
                sorted_arr.append(prefix[i2])
                i2 += 1
            for i in range(l, r+1):
                prefix[i] = sorted_arr[i-l]
            return count
        
        return merge_sort_count(0, len(prefix)-1)