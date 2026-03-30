class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()

        for n in nums:
            if n not in dup_set:
                dup_set.add(n)
            else:
                return True
        return False
         


"""
Brute force: Looping through the array twice and checking if any of the other indexes are the same
Time: O(n^2), Space O(n)

Trade off reduces time complexity for addition space used

Using a set to check if an element already exists
Time: O(n) Space: O(n)
"""