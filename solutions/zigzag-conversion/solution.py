# Problem: Zigzag Conversion
# URL: https://leetcode.com/problems/zigzag-conversion/
# Language: python3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        i=0
        res=[""]*numRows
        up=1
        for ch in s:
            res[i]+=(ch)
            if i==0:
                up=1
            if i==numRows-1:
                up=-1
            i+=up
        
        return (''.join(res))