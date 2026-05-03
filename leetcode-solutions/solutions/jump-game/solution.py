# Problem: Jump Game
# URL: https://leetcode.com/problems/jump-game/
# Language: python3

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        farthest=0
        for i in range(n):
            if i > farthest:
                return False
            farthest=max(farthest,i+nums[i])
        return True