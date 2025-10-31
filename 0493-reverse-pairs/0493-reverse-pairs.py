class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort_count(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_sort_count(left, mid) + merge_sort_count(mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            nums[left:right + 1] = sorted(nums[left:right + 1])
            return count
        
        return merge_sort_count(0, len(nums) - 1)