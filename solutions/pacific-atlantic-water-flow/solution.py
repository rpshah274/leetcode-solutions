# Problem: Pacific Atlantic Water Flow
# URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Language: python3

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        res=[]
        pacific_visited = set()
        atlantic_visited = set()
        pacific=deque()
        atlantic=deque()
        for i in range(m):
            pacific.append((i,0))
            pacific_visited.add((i,0))
            atlantic.append((i,n-1))
            atlantic_visited.add((i,n-1))
        for j in range(n):
            pacific.append((0,j))
            pacific_visited.add((0,j))
            atlantic.append((m-1,j))
            atlantic_visited.add((m-1,j))
        def bfs(q,visited):   
            while q:
                r,c= q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if (0<=row<=(m-1) and 0<=col<=(n-1) and heights[row][col]>=heights[r][c] and (row, col) not in visited):
                        visited.add((row,col))
                        q.append((row, col))
            
        bfs(pacific, pacific_visited)
        bfs(atlantic, atlantic_visited)
        return list(pacific_visited & atlantic_visited)