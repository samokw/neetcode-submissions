class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a hashmap that keeps track of the count of the num
        numsFreq = {}
        freqArr = []
        result = []

        for num in nums:
            if num not in numsFreq:
                numsFreq[num] = 1
            else:
                numsFreq[num] += 1
        for num, count in numsFreq.items():
            freqArr.append([count, num])
        freqArr.sort()

        while len(result) < k:
            result.append(freqArr.pop()[1])
        return result
        
        

        