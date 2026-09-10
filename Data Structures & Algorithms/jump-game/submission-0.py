class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = len(nums) - 1
        curr = 0

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal < 1

            


