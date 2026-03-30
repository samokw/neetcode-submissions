class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap using defaultdict(list)
        # Loop through all the string
        # Within the loop Create an intaialized array with 26 spots
        # now loop through every character in that particular string
        # within this loop initailize the index of index using ord(c) - ord('a') incrementing by 1
        # now outside of this list use the hashmap the key being a tuple(array) appending the currString
        # make the overall code return a list(hashmap.values())
        result = defaultdict(list)
        for currStr in strs:
            letterCount = [0] * 26
            for currChr in currStr:
                letterCount[ord(currChr) - ord("a")] += 1
            result[tuple(letterCount)].append(currStr)
        return list(result.values())
