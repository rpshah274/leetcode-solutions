# Problem: Step-By-Step Directions From a Binary Tree Node to Another
# URL: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Language: python3

from typing import Optional
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node,path,target):
            if not node:
                return False
            if node.val==target:
                return True
            path.append('L')
            if dfs(node.left,path,target):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right,path,target):
                return True
            path.pop()

            return False
            
        path_start=[]
        path_end=[]

        dfs(root,path_start,startValue)
        dfs(root,path_end,destValue)

        i=0
        while i<len(path_start) and i<len(path_end) and path_start[i]==path_end[i]:
            i+=1
        
        return ''.join(['U']*len(path_start[i:])+path_end[i:] )
