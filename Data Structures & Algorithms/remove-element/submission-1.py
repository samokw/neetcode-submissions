class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        R = len(nums)

        # THE L pointer will be used to find the target values that need to be swapped
        while L < R:
            if nums[L] == val:
                R -= 1
                nums[L] = nums[R]
            else:
                L += 1
        return R