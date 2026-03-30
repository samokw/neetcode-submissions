class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if two lists are the same length
        #Use a hashmap {'letter': count}
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #Increases the count, or if hasn't been set makes it zero
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT # checking if the hashmaps are the same
  
