# Problem: Sum of Distances
# URL: https://leetcode.com/problems/sum-of-distances/
# Language: python3

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        n = len(nums)
        res = [0] * n
        for i, num in enumerate(nums):
            groups[num].append(i)
        for arr in groups.values():
            total=sum(arr)
            count=len(arr)
            sum_left=0
            count_left=0
            for i,idx in enumerate(arr):
                sum_right=total-sum_left-idx
                count_right=count-count_left-1
                l=i*arr[i]-sum_left
                r=sum_right-(count_right)*idx
                res[idx]=l+r
                sum_left += idx
                count_left += 1
        return res
