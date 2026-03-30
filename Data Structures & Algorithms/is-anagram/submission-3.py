class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map  = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        
        for char in s:
            s_map[char] +=1
        for char in t:
            t_map[char] += 1
        if s_map == t_map:
            return True
        return False