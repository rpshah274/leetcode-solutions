# Problem: Longest Mountain in Array
# URL: https://leetcode.com/problems/longest-mountain-in-array/
# Language: python3

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i=1
        res=0
        if len(arr)<3:
            return 0
        while i<(len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                l=i-1
                r=i+1
                while l > 0  and arr[l]>arr[l-1]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                res=max(res,r-l+1)
                i=r
            i+=1
        return res