# Problem: Rotate Function
# URL: https://leetcode.com/problems/rotate-function/
# Language: python3

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        k = len(nums)
        total=sum(nums)
        F = sum(i * nums[i] for i in range(k))
        res= F
        
        for i in range(1,k):
            F=F+total-k*nums[k-i]
            res=max(res,F)  
        return res
        