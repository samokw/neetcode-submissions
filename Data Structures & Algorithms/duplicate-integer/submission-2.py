class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create a set, this keeps tracks of the numbers we have seen
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False

        
         