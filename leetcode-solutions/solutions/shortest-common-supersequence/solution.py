# Problem: Shortest Common Supersequence 
# URL: https://leetcode.com/problems/shortest-common-supersequence/
# Language: python3

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        res=""
        i,j=m,n
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                res+=str1[i-1]
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    res+=str2[j-1]
                    j-=1
                else:
                    res+=str1[i-1]
                    i-=1
        while i>0:
            res+=str1[i-1]
            i-=1
        while j>0:
            res+=str2[j-1]
            j-=1
        return res[::-1]
