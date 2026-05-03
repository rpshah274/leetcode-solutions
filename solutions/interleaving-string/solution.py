# Problem: Interleaving String
# URL: https://leetcode.com/problems/interleaving-string/
# Language: python3

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s3)!=len(s1)+len(s2):
            return False
        n=len(s1)
        m=len(s2)
        i=0
        j=0
        dp=[[None]*(m+1) for _ in range(n+1)]
        def dfs(i,j):
            if i==n and j==m:
                return True
            if dp[i][j] is not None:
                return dp[i][j]
            if i<n and s1[i]==s3[i+j] and dfs(i+1,j):
                return True
            if j<m and s2[j]==s3[i+j] and dfs(i,j+1):
                return True
            dp[i][j]=False
            return False
        return dfs(0,0)

