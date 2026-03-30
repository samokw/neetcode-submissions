class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        n = len(nums)

        for i in range(n - 2): # We dont to choose one number for i not including the last two
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            L, R = i + 1, n - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    R -= 1
                    while nums[R] == nums[R + 1] and R > L:
                        R -= 1
        return res