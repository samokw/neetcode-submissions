class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            if i > 0 and anchor == nums[i - 1]:
                continue 
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = anchor + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([anchor, nums[L], nums[R]])
                    L += 1 
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res