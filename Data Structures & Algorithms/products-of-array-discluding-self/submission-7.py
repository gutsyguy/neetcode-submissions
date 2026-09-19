class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= prefix
            res[-1 - i] *= suffix

            prefix *= nums[i]
            suffix *= nums[-1 - i]
        
        return res
        