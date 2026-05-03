# Problem: Maximum Product Subarray
# URL: https://leetcode.com/problems/maximum-product-subarray/
# Language: python3

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        mini=1
        maxi=1
        for n in nums:
            if n==0:
                mini=1
                maxi=1
                continue
            temp=maxi*n
            maxi=max(n,mini*n,maxi*n)
            mini=min(n,mini*n,temp)
            res=max(res,maxi)
        return res