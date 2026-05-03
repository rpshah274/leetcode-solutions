# Problem: Valid Parenthesis String
# URL: https://leetcode.com/problems/valid-parenthesis-string/
# Language: python3

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        stack_star=[]
        for i in range(len(s)):
            ch=s[i]
            if ch=='(':
                stack.append([ch,i])
            if ch==')':
                if not stack and not stack_star:
                    return False
                if stack:
                    if stack[-1][0]=='(' and stack[-1][1]<i:
                        stack.pop()
                elif stack_star[-1]<i:
                    stack_star.pop()
            if ch=='*':
                stack_star.append(i)
        while stack and stack_star:
            if stack_star[-1] > stack[-1][1]:
                stack.pop()
                stack_star.pop()
            else:
                return False
        return not stack
