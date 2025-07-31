class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 3: Find element just larger than nums[i] to the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 4: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: Reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
