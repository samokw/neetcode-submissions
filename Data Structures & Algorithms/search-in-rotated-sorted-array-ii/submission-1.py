class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return false
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            # If the left portion is sorted
            if nums[mid] > nums[low]:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            # It could be the case that right portion could be sorted
            elif nums[mid] < nums[low]:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            # We have repeating numbers in our comaparison so we need to move a pointer
            else:
                low += 1
        return False

