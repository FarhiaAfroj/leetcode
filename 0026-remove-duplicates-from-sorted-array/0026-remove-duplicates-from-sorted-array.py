class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        # 'i' tracks the position of the last unique element
        i = 0
        # Scan with 'j' from 1 to end
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        # The count of unique elements is i + 1
        return i + 1
