# Problem: Last Stone Weight II
# URL: https://leetcode.com/problems/last-stone-weight-ii/
# Language: python3

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=0
        for n in stones:
            total+=n
                
        s=len(stones)
        sub_sum=(total)//2
        #1D DP
        dp=[False]*(sub_sum+1) 
        dp[0]=True
        for n in stones:
            for i in range(sub_sum,n-1,-1):
                dp[i] = dp[i] or dp[i - n]
        for s in range(sub_sum,-1,-1):
            if dp[s]:
                return abs(2*s-total)