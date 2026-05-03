# Problem: Longest Palindromic Substring
# URL: https://leetcode.com/problems/longest-palindromic-substring/
# Language: python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start=0
        end=0
        n=len(s)
        def expand(i,j):
            while i>=0 and j<n and s[i]==s[j]: 
                i-=1
                j+=1
            return i+1,j-1
        for i in range(n):
            l1,r1=expand(i,i)
            l2,r2=expand(i,i+1)
            if r1-l1>end-start:
                start=l1
                end=r1
            if r2-l2>end-start:
                start=l2
                end=r2
        return s[start:end+1]