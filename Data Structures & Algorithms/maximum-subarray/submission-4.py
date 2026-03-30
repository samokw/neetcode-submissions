class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for n in nums:
            currSum += n
            currSum = max(currSum, n)
            maxSum = max(maxSum, currSum)
        return maxSum
        