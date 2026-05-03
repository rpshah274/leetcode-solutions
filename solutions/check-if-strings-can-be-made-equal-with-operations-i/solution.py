# Problem: Check if Strings Can be Made Equal With Operations I
# URL: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
# Language: python3

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_count=[0]*26
        odd_count=[0]*26
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if i%2==0:
                even_count[ord(s1[i]) - ord('a')] += 1
                even_count[ord(s2[i]) - ord('a')] -= 1
            else:
                odd_count[ord(s1[i]) - ord('a')] += 1
                odd_count[ord(s2[i]) - ord('a')] -= 1
        if even_count==[0]*26 and odd_count==[0]*26:
            return True
        return False