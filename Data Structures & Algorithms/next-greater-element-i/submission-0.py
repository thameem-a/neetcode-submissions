class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        output = []

        for n in nums1:
            # find where n is in nums2
            index = nums2.index(n)
            found = False

            for j in range(index + 1, len(nums2)):
                if nums2[j] > n:
                    output.append(nums2[j])
                    found = True
                    break

            if not found:
                output.append(-1)

        return output
                

