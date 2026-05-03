# Problem: Sort Integers by The Power Value
# URL: https://leetcode.com/problems/sort-integers-by-the-power-value/
# Language: python3

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x==1:
                return 0
            res=0
            if x%2==0:
                res=1+power(x/2)
            else:
                res=1+power(3*x+1)
            return res
        result=[]
        for n in range(lo,hi+1):
            result.append([power(n),n])
        result.sort()
        return result[k-1][1]