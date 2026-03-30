class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                index = 0
                while n + index in num_set:
                    index += 1
                longest = max(longest, index)
        return longest

        