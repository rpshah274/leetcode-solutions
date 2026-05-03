# Problem: Spiral Matrix
# URL: https://leetcode.com/problems/spiral-matrix/
# Language: python3

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        length=len(matrix)*len(matrix[0])
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
            bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
            left += 1
        return ans