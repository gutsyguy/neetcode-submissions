class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set = (nums)
        consecutive = 0

        for num in nums:
            count = 1
            streak = 1
            while num - count in set:
                streak += 1
                count += 1
            consecutive = max(count, consecutive)
        return consecutive
                

        