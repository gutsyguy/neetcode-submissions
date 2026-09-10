class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for num in nums:
            local_max = 1
            while num - 1 in seen:
                local_max += 1
                num = num - 1

            max_len = max(max_len, local_max)

        return max_len
        