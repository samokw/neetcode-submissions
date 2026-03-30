class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_ending = max_sum = nums[0]
        min_ending = min_sum = nums[0]

        for n in nums[1:]:
            max_ending = max(max_ending + n, n)
            max_sum = max(max_sum, max_ending)

            min_ending = min(min_ending + n, n)
            min_sum = min(min_sum, min_ending)


        # if all the best sum we could find is negative return the largest one we found
        if max_sum < 0:
            return max_sum
        
        # otherwise we can return best sum we found (without wrap (max_sum) or with thr wrap (total - min_sum))
        return max(max_sum, total - min_sum)
