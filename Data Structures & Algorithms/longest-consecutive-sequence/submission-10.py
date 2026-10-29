class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            if num - 1 in seen:
                continue
            else:
                curr = 1
                while num + 1 in seen:
                    curr += 1
                    num += 1
                res = max(curr, res)

        return res
        