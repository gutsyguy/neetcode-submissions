class Solution:
    def rob(self, nums: List[int]) -> int:
        cash1 = 0
        cash2 = 0

        for num in nums:
            temp = max(cash1 + num, cash2)
            cash1 = cash2
            cash2 = temp

        return cash2
        