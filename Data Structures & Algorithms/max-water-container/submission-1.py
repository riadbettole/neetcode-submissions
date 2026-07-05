class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights) - 1
        while l < r:
            minim = min(heights[l], heights[r])
            prod = minim * ( r - l )
            maximum = max(maximum, prod)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return maximum