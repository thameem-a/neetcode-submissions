class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Step 1: store product of everything to the right
        suffix = [1] * n
        running_product = 1

        for i in range(n - 1, -1, -1):
            suffix[i] = running_product
            running_product *= nums[i]

        # Step 2: keep track of product to the left
        output = [1] * n
        running_product = 1

        for i in range(n):
            output[i] = running_product * suffix[i]
            running_product *= nums[i]

        return output
