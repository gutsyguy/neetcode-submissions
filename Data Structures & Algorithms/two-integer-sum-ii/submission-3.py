class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        groups = {}

        for i, n in enumerate(numbers):
            complement = target - n

            if n in groups:
                return [groups[n] + 1, i+1]

            groups[complement] = i

