# Problem: Construct Product Matrix
# URL: https://leetcode.com/problems/construct-product-matrix/
# Language: python3

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m=len(grid),len(grid[0])
        mod=12345
        prefix=1
        ans=[[1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = (ans[i][j] * prefix) % mod
                prefix = (prefix * grid[i][j]) % mod
        suffix=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans[i][j] = (ans[i][j] * suffix) % mod
                suffix = (suffix * grid[i][j]) % mod
        return ans