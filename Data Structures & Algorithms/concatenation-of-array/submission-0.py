from copy import deepcopy

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = deepcopy(nums)

        for i in nums:
            copy.append(i)
        return copy
        