class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers:
        i = m - 1       # Last original element in nums1
        j = n - 1       # Last element in nums2
        k = m + n - 1   # Last position in nums1 (end buffer)

        # Merge until nums2 is fully inserted
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
