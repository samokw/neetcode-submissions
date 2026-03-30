class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxArea = 0
        while L < R:
            minHeight = min(heights[L], heights[R])
            area = minHeight * (R - L)
            maxArea = max(maxArea, area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxArea
        