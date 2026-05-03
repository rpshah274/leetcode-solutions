# Problem: Combinations
# URL: https://leetcode.com/problems/combinations/
# Language: python3

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        sol=[]
        def backtrack(x):
            if len(sol)==k:
                res.append(sol[:])
                return 
            left=x
            need=k-len(sol)

            sol.append(x)
            backtrack(x-1)

            sol.pop()
            if left>need:
                backtrack(x-1)
        backtrack(n)
        return res

            