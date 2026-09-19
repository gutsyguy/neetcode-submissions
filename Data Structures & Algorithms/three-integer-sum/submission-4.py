class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if nums[i] > 0:
                    break
                
            if i > 0 and nums[i] == nums[i - 1]:
                    continue

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return list(res)
        