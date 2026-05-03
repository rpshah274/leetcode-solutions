# Problem: Word Break
# URL: https://leetcode.com/problems/word-break/
# Language: python3

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        n=len(s)
        memo={}
        def solve(i):
            if i==n:
                return True
            if i in memo:
                return memo[i]
            for j in range(i+1,n+1):
                if s[i:j] in wordDict and solve(j):
                    memo[i]=True
                    return True
            memo[i]=False
            return False
        return solve(0)