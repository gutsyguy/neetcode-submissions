class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        """
        {
            4: 0
            3: 1
        }
        """

        for i, num in enumerate(nums):
            complement = target - num
            if num in seen:
                return [seen[num], i]
            seen[complement] = i
