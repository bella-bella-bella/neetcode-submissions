class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        l, r = 0, len(heights) - 1

        while l < r:
            height_l, height_r = heights[l], heights[r]

            amt = (r - l) * min(height_l, height_r)
            max_amt = max(max_amt, amt)

            if height_l <= height_r:
                l += 1
            else:
                r -= 1
        
        return max_amt


