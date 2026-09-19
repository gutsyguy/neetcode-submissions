class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in seen:
                continue
            else:
                curr = 1
                while num + 1 in seen:
                    num = num + 1
                    curr += 1
                longest = max(longest, curr)

        return longest
        