class MedianFinder:

    def __init__(self):
        self.smaller = [] # Max Heap 
        self.larger = [] # Min Heap
        

    def addNum(self, num: int) -> None:
        # We always want to start with the element in the smaller heap and figure it out from there
        heapq.heappush(self.smaller, -1 * num)
        # If we have something in both heaps and the element in the max element in the smaller heap is larger than the min in the min element in the larger heap pop and add to the other heap
        if (self.smaller and self.larger and (-1 * self.smaller[0] > self.larger[0])):
            val = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        if len(self.smaller) > len(self.larger) + 1:
            val = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        if len(self.larger) > len(self.smaller) + 1:
            val = -1 * heapq.heappop(self.larger)
            heapq.heappush(self.smaller, val)

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -1 * self.smaller[0]
        elif len(self.smaller) < len(self.larger):
            return self.larger[0]
        else:
            return (-1 * self.smaller[0] + self.larger[0]) / 2
        