
class MedianFinder:

    def __init__(self):
        self.heapMax = []
        self.heapMin = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heapMax, -num)
        
        val = -heapq.heappop(self.heapMax)
        heapq.heappush(self.heapMin, val)
        
        if len(self.heapMin) > len(self.heapMax):
            val = heapq.heappop(self.heapMin)
            heapq.heappush(self.heapMax, -val)

    def findMedian(self) -> float:
        if len(self.heapMax) > len(self.heapMin):
            return -self.heapMax[0]
        return (-self.heapMax[0] + self.heapMin[0]) / 2.0
            