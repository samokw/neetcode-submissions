class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #Brute force solution 
        #sumList = []
        #for i in range(len(nums)):
        #    for j in range(len(nums)):
         #       if i != j:
          #          if nums[i] + nums[j] == target:
           #             sumList.append(i)
            #            sumList.append(j)
             #           return sumList
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        