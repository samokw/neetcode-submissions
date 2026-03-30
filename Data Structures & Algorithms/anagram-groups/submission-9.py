class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - we need to figure out the which strings have the same set of characters
        - all characters are lowercase
        - we can hash the string using ord(current_letter) - ord('a')
        - create a default dictionary with the value being a list with the hash turned into a tuple as the key and the value being a list of words that belong in with that key
        - we can the return a list(of dict.values())
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        result = {}
        
        """
        result = defaultdict(list)
        for s in strs:
            s_hash = [0] * 26
            for char in s:
                s_hash[ord(char) - ord('a')] += 1
            result[tuple(s_hash)].append(s)
        
        return list(result.values())
        