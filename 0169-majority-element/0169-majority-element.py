class Solution:
    def majorityElement(self, nums):
        """
        Boyer-Moore majority vote algorithm (no type hints so it's compatible
        with Python 2 and Python 3 judge environments).
        Assumes a majority element always exists (per problem statement).
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Optional quick local tests
if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))           # -> 3
    print(Solution().majorityElement([2,2,1,1,1,2,2]))    # -> 2
