class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        suffix = 1
        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            res[-1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[-1 - i]

        return res
        