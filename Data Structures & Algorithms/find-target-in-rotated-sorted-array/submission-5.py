class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
           return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            print(mid, low, high)
            if nums[mid] == target:
                return mid
            # We want to check is the left side is sorted nums[mid] >= nums[low] if thats the case
            if nums[mid] >= nums[low]:
                # If the target is somewhere between the mid index and low we cam get rid of the right half
                if nums[mid] >= target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            # If the left isnt sorted the right side must be
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1