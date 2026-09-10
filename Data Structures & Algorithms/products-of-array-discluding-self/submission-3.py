class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
            Understand: The objective here is to return an array where the value
            is the product of every value inside the nums array except nums[i]

            Plan:
                - First store the product of all the values before nums[i] in one array
                - Store the product of all the numbers after nums[i] in another array
                - Multiply the two arrays to get a final array that should contain the
                right answer.
        """

        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        prefix_product = 1
        suffix_product = 1


        for i in range(len(nums)):
            prefixes[i] = prefix_product
            suffixes[len(nums) - 1 - i] = suffix_product

            prefix_product *= nums[i]
            suffix_product *= nums[len(nums) - 1 - i]

        res = []

        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[i])

        return res

        print(prefixes)
        print(suffixes)



        