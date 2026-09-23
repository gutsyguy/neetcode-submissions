class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
            
        first_nums = nums[0: len(nums) - 1]
        last_nums = nums[1 : len(nums)]

        return max(self.helper(first_nums), self.helper(last_nums))

    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for i in range(len(nums)):
            new_rob = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = new_rob

        return rob2
        