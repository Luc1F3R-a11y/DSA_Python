class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        start = 1
        for i in range(2, n):
            if nums[i] != nums[i - 2]:
                nums[start] = nums[i]
                start += 1
        return start+1