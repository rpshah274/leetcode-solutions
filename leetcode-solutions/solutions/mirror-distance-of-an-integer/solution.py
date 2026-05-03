# Problem: Mirror Distance of an Integer
# URL: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Language: python3

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-int(str(n)[::-1]))