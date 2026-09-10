class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Understand:
                - I have to find the indices of the two numbers inside an array
                that add up to the target
                - There will always be 1 pair of numbers inside the array that
                add up to the target
                - return the smaller index first
                - i cannot equal j
            Plan:
                - Subtract the current number from the target to find
                the number we need in order to add up to the target
                - Store this in a hashmap with the number as the key
                and the index as the value
                - Go to the next one and if that number is found then return
                the two indexes
        """

        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i

        return -1



