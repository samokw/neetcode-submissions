class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We need to create a max heap so will negate the weights of the stones
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones) 
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])