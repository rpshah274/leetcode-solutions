# Problem: Rotting Oranges
# URL: https://leetcode.com/problems/rotting-oranges/
# Language: python3

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0
        time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            l=len(q)
            for i in range(l):
                r,c=q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if (row in range(m) and col in range(n) and grid[row][col]==1):
                        grid[row][col]=2
                        fresh-=1
                        q.append((row,col))
            time+=1
        return time if fresh==0 else -1