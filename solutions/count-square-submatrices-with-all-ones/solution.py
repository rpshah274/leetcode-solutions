# Problem: Count Square Submatrices with All Ones
# URL: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Language: python3

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if i>=m or j>=n or matrix[i][j]==0:
                return 0
            else:
                if dp[i][j]!=-1:
                    return dp[i][j]    
                r=solve(i,j+1)
                b=solve(i+1,j)
                d=solve(i+1,j+1)
                dp[i][j]=1+min(r,b,d)
                return dp[i][j]
        res=0
        for i in range(m):
            for j in range(n):
                res+=solve(i,j)
        return res