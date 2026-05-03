# Problem: Time Based Key-Value Store
# URL: https://leetcode.com/problems/time-based-key-value-store/
# Language: python3

class TimeMap:

    def __init__(self):
        self.TimeMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""  
        arr = self.TimeMap[key]
        l, r = 0, len(arr) - 1
        res = ""
        while l<=r:
            mid=(l+r)//2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
                   



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)