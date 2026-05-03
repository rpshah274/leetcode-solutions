# Problem: Valid Sudoku
# URL: https://leetcode.com/problems/valid-sudoku/
# Language: python3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_freq=[[False]* 9 for _ in range(9)]
        col_freq=[[False]* 9 for _ in range(9)]
        grid_freq=[[False]* 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=ord(board[i][j])-ord('1')
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if row_freq[i][num] or col_freq[num][j] or grid_freq[boxIndex][num]:
                        return False
                    row_freq[i][num] = col_freq[num][j] = grid_freq[boxIndex][num] = True
        return True