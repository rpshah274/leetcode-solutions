# Problem: Intervals Between Identical Elements
# URL: https://leetcode.com/problems/intervals-between-identical-elements/
# Language: python3

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        groups=defaultdict(list)
        n=len(arr)
        res=[0]*n
        for i,n in enumerate(arr):
            groups[n].append(i)
        for group in groups.values():
            total=sum(group)
            count=len(group)
            sum_left=0
            count_left=0
            for i,idx in enumerate(group):
                sum_right=total-sum_left-idx
                count_right=count-count_left-1
                l=i*group[i]-sum_left
                r=sum_right-(count_right)*idx
                res[idx]=l+r
                sum_left+=idx
                count_left+=1
        return res