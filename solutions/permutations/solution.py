# Problem: Permutations
# URL: https://leetcode.com/problems/permutations/
# Language: python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        sol=[]
        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res