# Problem: Check if Strings Can be Made Equal With Operations II
# URL: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# Language: python3

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
        # even_count=[0]*26
        # odd_count=[0]*26
        # if len(s1)!=len(s2):
        #     return False
        # for i in range(len(s1)):
        #     if i%2==0:
        #         even_count[ord(s1[i]) - ord('a')] += 1
        #         even_count[ord(s2[i]) - ord('a')] -= 1
        #     else:
        #         odd_count[ord(s1[i]) - ord('a')] += 1
        #         odd_count[ord(s2[i]) - ord('a')] -= 1
        # if odd_count==[0]*26 and even_count==[0]*26:
        #     return True
        # else:
        #     return False