class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            smaller_wall = min(heights[l], heights[r])
            max_vol = max(max_vol, smaller_wall * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_vol