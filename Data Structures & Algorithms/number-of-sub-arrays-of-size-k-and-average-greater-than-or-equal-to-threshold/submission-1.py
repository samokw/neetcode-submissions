class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_threshold = threshold * k
        L = 0
        res = 0
        curr_sum = 0
        for R in range(len(arr)):
            curr_sum += arr[R]
            if R - L + 1 > k:
                curr_sum -= arr[L]
                L += 1
            if curr_sum//k >= threshold and R - L + 1 == k:
                res += 1
        return res