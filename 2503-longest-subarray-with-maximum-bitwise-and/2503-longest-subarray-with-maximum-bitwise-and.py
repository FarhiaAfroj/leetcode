class Solution:
    def longestSubarray(self, nums):
        # Find the maximum value in nums
        max_val = max(nums)
        max_len = 0
        curr = 0
        
        # Traverse array
        for x in nums:
            if x == max_val:
                curr += 1
                if curr > max_len:
                    max_len = curr
            else:
                curr = 0
        
        return max_len

# Example usage:
if __name__ == "__main__":
    print(Solution().longestSubarray([1, 2, 3, 3, 2, 2]))  # Output: 2
    print(Solution().longestSubarray([1, 2, 3, 4]))        # Output: 1
