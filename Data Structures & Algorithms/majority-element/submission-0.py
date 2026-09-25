class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # key is n and value in frequency 
        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        return max(seen, key = seen.get)
