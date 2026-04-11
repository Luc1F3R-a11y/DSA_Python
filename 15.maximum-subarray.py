class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = 0
        max_sum = nums[0]

        for i in range(n):
            current_sum = nums[i]
            if current_sum < 0:
                max_sum = 0
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum

