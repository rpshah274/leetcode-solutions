# Problem: Combination Sum
# URL: https://leetcode.com/problems/combination-sum/
# Language: python3

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(candidates)
        def backtrack(start, remain, path):
            if remain==0:
                res.append(sol[:])
                return
            if start==n:
                return   
            #Take
            if candidates[start]<=remain:
                sol.append(candidates[start])
                backtrack(start,remain-candidates[start],sol) 
                sol.pop()
            #Not Take  
            backtrack(start+1,remain,sol)  

        backtrack(0,target,sol) 
        return res   