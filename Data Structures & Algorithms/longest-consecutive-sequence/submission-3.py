class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for num in seen:
            if num - 1 not in seen:
                curr = num
                local_max = 1

                while curr + 1 in seen:
                    curr += 1
                    local_max += 1

                max_len = max(max_len, local_max)
                
        return max_len
            