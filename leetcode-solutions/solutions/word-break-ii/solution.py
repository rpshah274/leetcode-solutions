# Problem: Word Break II
# URL: https://leetcode.com/problems/word-break-ii/
# Language: python3

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        memo={}
        n=len(s)

        def solve(i):
            if i==n:
                return [""]
            if i in memo:
                return memo[i]
            
            res=[]
            for j in range(i+1,n+1):
                word=s[i:j]

                if word in wordDict:
                    for sub in solve(j):
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word+ " "+sub)
            memo[i]=res
            return res
        return solve(0)