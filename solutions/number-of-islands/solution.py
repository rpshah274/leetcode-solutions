# Problem: Number of Islands
# URL: https://leetcode.com/problems/number-of-islands/
# Language: python3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if not (0<=r<m and 0<=c<n) or grid[r][c]=='0': #Do nothing 
                return
            grid[r][c]='0' #Mark it Zero

            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count
        # m=len(grid)
        # n=len(grid[0])
        # count=0
        # directions=[(0,1),(1,0),(-1,0),(0,-1)]
        # def bfs(r,c):
        #     q=deque()
        #     q.append((r,c))
        #     grid[r][c]="0"
        #     while q:
        #         l=len(q)
        #         for _ in range(l):
        #             r,c=q.popleft()
        #             for dr,dc in directions: 
        #                 row=r+dr
        #                 col=c+dc
        #                 if (row in range(m) and col in range(n) and grid[row][col]=="1"):
        #                     grid[row][col] = "0"
        #                     q.append((row, col))
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]=="1":
        #             count+=1
        #             bfs(i,j)
        # return count