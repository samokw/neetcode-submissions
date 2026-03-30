class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L, max_substring = 0, 0

        for R in range(len(s)):
            freq[s[R]] = 1 + freq.get(s[R], 0)
            # length of string - the most common element > num of changes we can make
            while (R - L + 1) - max(freq.values()) > k:
                freq[s[L]] -= 1
                L += 1
            max_substring = max(max_substring, R - L + 1)
        
        return max_substring