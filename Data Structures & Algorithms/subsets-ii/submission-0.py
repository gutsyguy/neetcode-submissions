class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()

        def backtrack(i, path):
            if i >= len(nums):
                seen.add(tuple(path.copy()))
                return

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            backtrack(i + 1, path)

        backtrack(0, [])

        return list(seen)
        