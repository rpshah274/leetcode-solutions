# Problem: Count Indices With Opposite Parity
# URL: https://leetcode.com/problems/count-indices-with-opposite-parity/
# Language: python3

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n
        even=0
        odd=0
        for i in range(n-1,-1,-1):
            if nums[i]%2==0:
                res[i]=odd
                even+=1
            else:
                res[i]=even
                odd+=1 
        return res
            