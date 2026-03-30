class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            word_hash = [0] * 26
            for char in s:
                word_hash[ord(char) - ord('a')] += 1
            anagrams[tuple(word_hash)].append(s)
        return list(anagrams.values())