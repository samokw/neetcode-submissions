class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in m:
                return [m[diff], i]
            else:
                m[n] = i


"""
Input: nums = [4,5,6], target = 10

Output: [0,2]

key -> value
number -> index


"""       