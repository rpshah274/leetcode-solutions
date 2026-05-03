# Problem: Subsets
# URL: https://leetcode.com/problems/subsets/
# Language: python3

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        sol=[]
        def backtrack(i):
            if i>=n:
                res.append(sol.copy())
                return
            #Taken
            sol.append(nums[i])
            backtrack(i+1)

            #Not Taken
            sol.pop()
            backtrack(i+1)

        backtrack(0)
        return res


