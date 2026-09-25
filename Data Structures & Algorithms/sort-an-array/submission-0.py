class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            # last i elements are already in place, no need to re-check them
            for j in range(0, len(nums) - i - 1):
                # swap if the element found is greater than the next element
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
