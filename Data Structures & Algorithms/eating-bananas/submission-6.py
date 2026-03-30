class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            k = low + (high - low) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/k)
            if total_time <= h:
                ans = k
                high = k - 1
            else:
                low = k + 1
        return ans

