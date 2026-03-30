class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        [1, 1, 2, 3, 4]
        for i in range(len(nums)):
            if val != nums[i]:
                nums[L] = nums[i]
                L += 1
        return L