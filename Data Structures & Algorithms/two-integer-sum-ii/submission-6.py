class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if target == total:
                return [L + 1, R + 1]
            elif target > total:
                L += 1
            else:
                R -= 1
            