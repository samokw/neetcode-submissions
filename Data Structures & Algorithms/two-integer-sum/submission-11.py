class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}

        for index, num in enumerate(nums):
            value_map[num] = index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in value_map and value_map[diff] != index:
                return [index, value_map[diff]]