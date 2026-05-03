# Problem: Angles of a Triangle
# URL: https://leetcode.com/problems/angles-of-a-triangle/
# Language: python3

import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        if (sides[0]+sides[1]<=sides[2]) or (sides[0]+sides[2]<=sides[1]) or (sides[2]+sides[1]<=sides[0]):
            return []
        def solve(a,b,c):
            cos_c=(a**2+b**2-c**2)/(2*a*b)
            return math.degrees(math.acos(cos_c))
        x1=solve(sides[0],sides[1],sides[2])
        x2=solve(sides[0],sides[2],sides[1])
        x3=solve(sides[2],sides[1],sides[0])
        
        res=[x1,x2,x3]
        
        return sorted(res)