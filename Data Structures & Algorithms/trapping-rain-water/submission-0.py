class Solution:
    def trap(self, height: List[int]) -> int:
        max_L = max_R = trapped = 0
        L, R = 0, len(height) - 1

        while L < R:
            curr_L, curr_R = height[L], height[R]
            max_L = max(max_L, curr_L)
            max_R = max(max_R, curr_R)

            if max_L < max_R:
                trapped += max_L - curr_L
                L += 1
            else:
                trapped += max_R - curr_R
                R -= 1
        return trapped