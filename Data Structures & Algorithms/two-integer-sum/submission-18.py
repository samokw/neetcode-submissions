class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - we want the sum of two numbers that sum up to the target, and that are not the same indices
        - the pair will exist in the loop
        - we would use two for loops, with an condition to check if we found the target when i != j
        - this optimizes for space but is O(n^2) time complexity
        - alternatively we would build a kinda of cache of what we've seen, so far along with the indexes using a dictionary
        - the key would be the amount we need to add to that number to get to the target, while the value would be the index
        nums = [3,4,5,6], target = 7

        
        Input: nums = [4,5,6], target = 10
        i = 1
        num = 6
        diff = 4
        cache = {4:0, 5:1, }
        """
        cache = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [cache[diff], i]
            cache[num] = i
