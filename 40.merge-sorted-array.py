class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i < 0 or nums[j] > nums[i]:
                nums[k] = nums[j]
                j -= 1
                k -= 1
            else:
                nums[k] = nums[i]
                i -= 1
                k -= 1
        return nums
