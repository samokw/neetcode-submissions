class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_window, curr = 0, 0
        for n in nums:
            if n == 1:
                curr += 1
            else:
                curr = 0
            max_window = max(max_window, curr)
        return max_window