# Problem: Data Stream as Disjoint Intervals
# URL: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Language: python3

class SummaryRanges:

    def __init__(self):
        self.arr=[]
    def addNum(self, value: int) -> None:
        self.arr.append(value)
    def getIntervals(self) -> List[List[int]]:
        if not self.arr:
            return []
        self.arr.sort()
        n = len(self.arr)
        start = self.arr[0]
        res = []
        for i in range(1,n):
            if self.arr[i] - self.arr[i-1] >1:
                res.append([start, self.arr[i-1]])
                start = self.arr[i]
        res.append([start,self.arr[n-1]])
        return res
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()