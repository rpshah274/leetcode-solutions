# Problem: Find the Degree of Each Vertex
# URL: https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Language: python3

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[0]*len(matrix)
        for i in range(len(matrix)):
            res[i]=sum(matrix[i])
        return res