class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # maxHeap
        self.largeHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        if len(self.smallHeap) > len(self.largeHeap):
            heapq.heappush(self.smallHeap, -num)
            left = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, left)
        else:   # len(small) == len(large)
            heapq.heappush(self.largeHeap, num)
            right = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -right)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2


        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()