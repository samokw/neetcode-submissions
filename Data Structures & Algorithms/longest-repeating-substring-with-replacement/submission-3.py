class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        maxSubstring = 0
        for R in range(len(s)):
            freq[s[R]] = 1 + freq.get(s[R], 0)
            while (R - L + 1) - max(freq.values()) > k:
                freq[s[L]] -= 1
                L += 1
            maxSubstring = max(maxSubstring, R - L + 1)
        return maxSubstring
        