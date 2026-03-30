class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        we know an anagram has the exactly the same characters as other string
        - they are the same length
        - we can create two hash tables of the letters they have and compare them together to see they are the same
        """
        if len(s) != len(t):
            return False
        
        s_hash = [0] * 26
        t_hash = [0] * 26

        for i in range(len(s)):
            s_hash[ord(s[i]) - ord('a')] += 1
            t_hash[ord(t[i]) - ord('a')] += 1
        
        return s_hash == t_hash
