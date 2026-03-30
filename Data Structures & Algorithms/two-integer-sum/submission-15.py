class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}

        for i, n in enumerate(nums):
            if n in comp_map:
                return [comp_map[n], i]
            diff = target - n
            comp_map[diff] = i
        


"""
Brute force Loop through the array twice and add up the two indexes excluding where i == j
and see if it equals the target sum.
Space: O(1), Time: O(n^2)

Hashmap:
use the hashmap keep track of the index of the complement
nums = [3,4,5,6], target = 7

Output: [0,1]

complement = target - num[i]

complement -> index in the hashmap

return the two index

"""