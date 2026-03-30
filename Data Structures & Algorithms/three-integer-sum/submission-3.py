class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # TC O(n logn) SC O(n)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # Check if the current num we are at is the same as the prev
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                three_sum = a + nums[L] + nums[R]
                if three_sum > 0:
                    R -= 1
                elif three_sum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    R -= 1
                    while nums[R] == nums[R + 1] and R > L:
                        R -= 1
        return res