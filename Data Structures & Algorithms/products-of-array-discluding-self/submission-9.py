class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [1] * n

        for i in range(n):
            res[i] *= prefix
            res[-1 - i] *= suffix

            prefix *= nums[i]
            suffix *= nums[-1 - i]

        return res
        