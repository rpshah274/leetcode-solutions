# Problem: Find Median from Data Stream
# URL: https://leetcode.com/problems/find-median-from-data-stream/
# Language: python3

class MedianFinder:
    def __init__(self):
        self.heap_min=[]
        self.heap_max=[]

    def addNum(self, num: int) -> None:
        if self.heap_max and num>self.heap_max[0]:
            heapq.heappush(self.heap_max,num)
        else:
            heapq.heappush(self.heap_min,-num)
        if len(self.heap_max)>len(self.heap_min):
            v=heapq.heappop(self.heap_max)
            heapq.heappush(self.heap_min,-1*v)
        if len(self.heap_max)<len(self.heap_min):
            v=heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max,-1*v)
            
    def findMedian(self) -> float:
        if len(self.heap_max)>len(self.heap_min):
            return self.heap_max[0]
        if len(self.heap_min)>len(self.heap_max):
            return -1*self.heap_min[0]
        return (self.heap_max[0] + (-1*self.heap_min[0]))/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()