class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # Loop through even index in the first string
            for s in strs: # Looping through all strings
                if i == len(s) or s[i] != strs[0][i]: # Chcek if the current string is the length of the index or the index is not a part of original string
                    return s[:i] # return the string up to that point
        return strs[0] # otherwise can return the 