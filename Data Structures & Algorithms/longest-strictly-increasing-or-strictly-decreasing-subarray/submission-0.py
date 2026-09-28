class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        increasing = 1  
        decreasing = 1 
        longest = 1 

        for i in range(len(nums) - 1 ):
            # decrease
            if nums[i] > nums[i + 1]:
                decreasing += 1
                increasing = 1
            # increasing
            elif nums[i] < nums[i + 1]:
                increasing += 1
                decreasing = 1
            else:
                increasing = 1 
                decreasing = 1 

            longest = max(increasing, decreasing, longest)
        return longest
