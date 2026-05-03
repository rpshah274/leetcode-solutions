# Problem: Max Area of Island
# URL: https://leetcode.com/problems/max-area-of-island/
# Language: python3

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #DFS
        m, n = len(grid), len(grid[0])
        def dfs(r,c):
            if not(0<=r<m and 0<=c<n) or grid[r][c]==0:
                return 0

            grid[r][c]=0
            return (1
            + dfs(r+1,c)+ dfs(r,c+1)
            + dfs(r-1,c)+ dfs(r,c-1))
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        return area       
        #BFS
        # m, n = len(grid), len(grid[0])
        # area = 0
        # directions = [(0,1),(1,0),(-1,0),(0,-1)]

        # def bfs(r, c):
        #     q=deque()
        #     q.append((r,c))
        #     grid[r][c]=0
        #     count=1
        #     while q:
        #         length=len(q)
        #         for i in range(length):
        #             r,c=q.popleft()
        #             for dr,dc in directions: 
        #                 row,col = r+dr,c+dc
        #                 if (row in range(m) and col in range(n) and 
        #                 grid[row][col]==1):
        #                     grid[row][col] = 0
        #                     count+=1
        #                     q.append((row, col))
        #     return count
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             area=max(area,bfs(i, j))
        # return area