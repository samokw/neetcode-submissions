class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0

        length, maxLength = 0, 0
        if len(s) == 1:
            return 1
        for R in range(len(s)):
            if s[R] in window:
                print(length)
                while s[R] in window:
                    window.remove(s[L])
                    maxLength = max(maxLength, length)
                    L += 1
                    length -= 1
                    print("l",L)
            window.add(s[R])
            length += 1
            maxLength = max(maxLength, length)
        return maxLength