class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import bisect
        
        def count(target):
            cnt = 0
            for x in nums1:
                if x == 0:
                    if target >= 0:
                        cnt += len(nums2)
                    continue
                    
                if x > 0:
                    threshold = target / x
                    idx = bisect.bisect_right(nums2, threshold)
                    cnt += idx
                else:
                    threshold = target / x
                    idx = bisect.bisect_left(nums2, threshold)
                    cnt += len(nums2) - idx
            return cnt

        left, right = -10**11, 10**11
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left