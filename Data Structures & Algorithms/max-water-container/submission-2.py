class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l = 0
        r = n - 1

        while l < r:
            min_wall = min(heights[l], heights[r])
            res = max(res, min_wall * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
        