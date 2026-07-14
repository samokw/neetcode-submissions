class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L, R = 0, len(nums)
        # L will find the numbers we need to swap (L = val)
        # R reps the number we need swap with, R will move closer to the start
        # of the array as when we find another L val we dont want to include as part of the array
        while L < R:
            if nums[L] == val:
                R -= 1
                nums[L] = nums[R]
            else:
                L += 1
        return R