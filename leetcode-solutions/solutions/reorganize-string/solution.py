# Problem: Reorganize String
# URL: https://leetcode.com/problems/reorganize-string/
# Language: python3

import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        heap=[]
        for ch,f in Counter(s).items():
            heapq.heappush_max(heap,(f,ch))
        res=""
        while heap:
            if len(heap)>=2:
                f1,ch1=heapq.heappop_max(heap)
                f2,ch2=heapq.heappop_max(heap)
                res+=ch1+ch2
                f1-=1
                f2-=1
                if f1>0:
                    heapq.heappush_max(heap,(f1,ch1))
                if f2>0:
                    heapq.heappush_max(heap,(f2,ch2))
            else:
                f1,ch1=heapq.heappop_max(heap)
                if f1>1:
                    return ""
                else:
                    res+=ch1
        return res