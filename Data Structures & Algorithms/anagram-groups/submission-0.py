class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list) 

        for s in strs: 
            count = [0] * 26 #Initializing values for all letters
            for c in s:
                count[ord(c) - ord("a")] += 1
                # Counts how many of each character are in a string
                # the index of count is determined by what letter it is
                # a being 0 z being 25
            answer[tuple(count)].append(s)
            #If a tuple matches it will add to a particular list
        return answer.values()

        # Big O notation: O(m * n)
        # m is the number of words
        # n is the average number of letters in the words