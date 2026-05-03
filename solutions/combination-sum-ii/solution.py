# Problem: Combination Sum II
# URL: https://leetcode.com/problems/combination-sum-ii/
# Language: python3

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        candidates=sorted(candidates)
        n=len(candidates)
        def backtract(start,remain):
            if remain==0:
                res.append(sol[:])
                return
            #Taken    
            for i in range(start,n):
                if i>start and candidates[i] == candidates[i - 1]:
                    continue   
                x=candidates[i]        
                if x<=remain:
                    sol.append(x)
                    backtract(i+1,remain-x)
                    sol.pop()
            #Not Taken
            # backtract(start+1,remain)
        backtract(0,target)
        return res 