# Problem: Equal Sum Grid Partition I
# URL: https://leetcode.com/problems/equal-sum-grid-partition-i/
# Language: python3

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        row_sum=[0]*m
        col_sum=[0]*n
        total=0
        for i in range(m):
            for j in range(n):
                row_sum[i]+=grid[i][j]
                col_sum[j]+=grid[i][j]
                total+=grid[i][j]
        #Horizontal cut
        H_sum=0
        for i in range(m-1):
            H_sum+=row_sum[i]
            if H_sum==(total/2):
                return True
        #Verticle cut         
        V_sum=0
        for j in range(n-1):
            V_sum+=col_sum[j]
            if V_sum==(total/2):
                return True
        return False