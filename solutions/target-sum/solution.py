# Problem: Target Sum
# URL: https://leetcode.com/problems/target-sum/
# Language: python3

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=0
        for n in nums:
            total+=n
        if (total+target)%2!=0 or abs(target) > total:
            return 0
        sub_sum=(total+target)//2
        n=len(nums)

        #1D DP
        dp=[0]*(sub_sum+1) 
        dp[0]=1
        for n in nums:
            for i in range(sub_sum,n-1,-1):
                dp[i] = dp[i] +  dp[i - n]
        return dp[sub_sum]
        #2D DP

        # dp=[[False]*(sub_sum+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=True
        # for i in range(1,n+1):
        #     for j in range(1,sub_sum+1):
        #         if nums[i-1]<=j:
        #             dp[i][j]=(dp[i-1][j] or dp[i-1][j-nums[i-1]])
        #         else:
        #             dp[i][j]=dp[i-1][j]
        # return dp[n][sub_sum]