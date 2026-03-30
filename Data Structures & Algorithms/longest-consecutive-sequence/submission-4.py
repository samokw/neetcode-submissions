class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        num_set = set(nums)
        for n in num_set:
            if (n - 1 ) not in num_set:
                curr_len = 1
                while n + curr_len in num_set:
                    curr_len += 1
                length = max(length, curr_len)
        return length