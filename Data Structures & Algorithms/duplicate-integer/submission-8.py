class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        nums = [1, 2, 3, 3]

        set = (1, 2, 3)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False