class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1 
        max_area = 0

        while L < R:
            curr_area = min(heights[R], heights[L]) * (R - L)
            max_area = max(max_area, curr_area)

            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1
        return max_area