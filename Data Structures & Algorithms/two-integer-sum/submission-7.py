class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Use a hashmap
        # Add all number to the hashmap
        # use enumerate for index and value
        numsMap = {}
        for i, num in enumerate(nums):
            numsMap[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsMap:
                if i != numsMap[diff]:
                    return [i , numsMap[diff]]


        