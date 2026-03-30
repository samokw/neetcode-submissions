class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #First we can check if the string are the same length, if they differ
        #They cannot be anagrams
        #hashmap to keep track of the character count in s and t 
        #we can check if the hasmaps are the same
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            sMap[char] += 1
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            tMap[char] += 1
        if sMap == tMap:
            return True
        return False

        