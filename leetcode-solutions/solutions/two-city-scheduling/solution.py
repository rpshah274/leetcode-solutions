# Problem: Two City Scheduling
# URL: https://leetcode.com/problems/two-city-scheduling/
# Language: python3

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        res=0
        n=len(costs)
        for i in range(n//2):
            res+=costs[i][0]
        for i in range(n//2,n):
            res+=costs[i][1]
        return res