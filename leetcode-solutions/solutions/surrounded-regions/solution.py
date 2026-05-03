# Problem: Surrounded Regions
# URL: https://leetcode.com/problems/surrounded-regions/
# Language: python3

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #DFS
        if not board:
            return
        n=len(board)
        m=len(board[0])
        def dfs(r,c):
            if not (0<=r<n and 0<=c<m) or board[r][c]!='O':
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)

        for i in range(n):
            for j in range(m):
                if (i in [0, n-1] or j in [0, m-1]) and board[i][j] == 'O':
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
        #BFS
        # if not board or not board[0]:
        #     return
        # n=len(board)
        # m=len(board[0])
        # directions=[(1,0),(0,1),(-1,0),(0,-1)]
        # q=deque()
        # for i in range(n):
        #     for j in range(m):
        #         if (i in [0, n-1] or j in [0, m-1]) and board[i][j] == 'O':
        #             q.append((i,j))
        #             board[i][j]='T'
        # while q:
        #     r,c=q.popleft()
        #     for dr,dc in directions:
        #         row=r+dr
        #         col=c+dc
        #         if (row in range(n) and col in range(m) and board[row][col]=='O'):
        #             board[row][col]='T'
        #             q.append((row, col))
        # for i in range(n):
        #     for j in range(m):
        #         if board[i][j]=='O':
        #             board[i][j]='X'
        #         if board[i][j]=='T':
        #             board[i][j]='O'
