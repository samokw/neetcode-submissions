class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()

        for n in nums:
            if n not in found:
                found.add(n)
            else:
                return True
        return False