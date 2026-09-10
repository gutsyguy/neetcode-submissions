class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)

        res = [1] * n 

        for i in range(n):
            res[i] *= prefix 
            res[n - 1 - i] *= suffix

            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

        return res