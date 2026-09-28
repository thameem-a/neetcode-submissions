class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        total = nums[0]
        max_total = nums[0]

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                total += nums[i + 1]
            else:
                total = nums[i + 1]

            max_total = max(max_total, total)

        return max_total