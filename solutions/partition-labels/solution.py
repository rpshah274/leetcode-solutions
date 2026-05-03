# Problem: Partition Labels
# URL: https://leetcode.com/problems/partition-labels/
# Language: python3

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_dict={}
        for i in range(len(s)):
            end_dict[s[i]]=i
        res=[]
        start=0
        end=0
        for k in range(len(s)):
            end = max(end, end_dict[s[k]])
            if k == end:
                res.append(end-start+1)
                start=k+1
            k+=1
        return res