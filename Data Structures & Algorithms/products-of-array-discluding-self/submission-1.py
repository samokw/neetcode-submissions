class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            res[i] *= left # Calculate prefix
            left *= nums[i] # Now include the current number for the next iteration
        
        right = 1
        for i in range(n - 1, -1 , -1):
            res[i] *= right # Calculate the suffix
            right *= nums[i] # Now include the current number for the next iteration
        
        return res