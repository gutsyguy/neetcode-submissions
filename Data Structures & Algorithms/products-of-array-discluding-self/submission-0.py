class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = 1
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(i + 1, len(nums)):
                product *= nums[j]
            product *= counter
            counter *= nums[i]
            res.append(product)
        return res
        
           
                
            

        