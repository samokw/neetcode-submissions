class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #I want to add the all the numbers to a hashset
        #if the number exists in the set already return false after all the numbers have been looped through
        #otherwise return true
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
        # Big O: O(n)