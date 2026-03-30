class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:]
        heapq.heapify(min_heap)
        for n in nums[k:]:
            heapq.heappop(min_heap)
        return min_heap[0]