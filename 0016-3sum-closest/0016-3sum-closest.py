class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if the current sum is closer
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match found
                    return current_sum
        
        return closest_sum
