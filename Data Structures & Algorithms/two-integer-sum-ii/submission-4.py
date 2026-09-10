class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            use r to find the largest number that is smaller than target:
            if l + r is less than target more l, if its greater than move r
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
            



