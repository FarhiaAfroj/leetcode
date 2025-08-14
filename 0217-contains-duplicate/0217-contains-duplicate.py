from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if any value appears at least twice in the array.
        Time Complexity: O(n) on average.
        Space Complexity: O(n).
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Local testing (remove or comment out this part before submission)
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))           # Expected: True
    print(sol.containsDuplicate([1, 2, 3, 4]))           # Expected: False
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected: True
