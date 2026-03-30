class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Creates a set of the numbers we have
        numSet = set(nums)
        #Keeps track of the Current longest sequence we have
        longest = 0
        #Loops through the numbers in the set
        for num in numSet:
            #Checking if the previous number is not in the set
            if (num - 1) not in numSet:
                #Start the length at 1
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        