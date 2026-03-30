class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        arr_min = float("inf")
        while low <= high:
            mid = low + (high - low) // 2
            print(mid, low, high)
            if nums[mid] >= nums[low]:
                arr_min = min(arr_min, nums[low])
                low = mid + 1
            else:
                arr_min = min(arr_min, nums[mid])
                high = mid - 1
        return arr_min
