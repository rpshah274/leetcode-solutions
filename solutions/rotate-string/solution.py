# Problem: Rotate String
# URL: https://leetcode.com/problems/rotate-string/
# Language: python3

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return goal in (s+s)