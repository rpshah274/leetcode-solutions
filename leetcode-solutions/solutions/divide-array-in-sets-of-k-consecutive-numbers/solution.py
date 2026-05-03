# Problem: Divide Array in Sets of K Consecutive Numbers
# URL: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# Language: python3

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        freq=Counter(nums)
        for x in sorted(nums):
            while freq[x]>0:
                for n in range(x,x+k):
                    if freq[n]==0:
                        return False
                    freq[n]-=1
        return True