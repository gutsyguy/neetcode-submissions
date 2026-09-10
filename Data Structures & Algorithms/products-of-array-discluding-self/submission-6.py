class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= prefix
            res[len(nums) - 1 - i] *= suffix
            suffix *= nums[len(nums) - 1 - i]
            prefix *= nums[i]

        return res
        