# Problem: House Robber II
# URL: https://leetcode.com/problems/house-robber-ii/
# Language: python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            p1,p2=0,0
            for n in arr:
                taken=n+p1
                not_taken=p2
                res=max(taken,not_taken)
                p1=p2
                p2=res
            return p2
        if len(nums)==1:
            return nums[0]
        return max(solve(nums[:-1]), solve(nums[1:]))