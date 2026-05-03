# Problem: Ones and Zeroes
# URL: https://leetcode.com/problems/ones-and-zeroes/
# Language: python3

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #0/1 knapsack
        capacity=(m,n)
        w=[]
        for st in strs:
            z=o=0
            for ch in st:
                if ch=='1':
                    o+=1
                else:
                    z+=1
            w.append((z,o))
        dp = [[0]*(n+1) for _ in range(m+1)]

        for z, o in w:
            for i in range(m, z-1, -1):      # backward
                for j in range(n, o-1, -1):  # backward
                    dp[i][j]= max(dp[i][j], 1 + dp[i-z][j-o])
        return dp[m][n]

