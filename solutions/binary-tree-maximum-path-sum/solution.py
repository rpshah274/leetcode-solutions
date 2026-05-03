# Problem: Binary Tree Maximum Path Sum
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result=float('-inf')
        def dfs(node):
            # nonlocal result
            if not node:
                return 0
            left_ans=max(dfs(node.left), 0)
            right_ans=max(dfs(node.right), 0)
            self.result = max(self.result, node.val + left_ans + right_ans)
            return max(left_ans,right_ans)+node.val
        dfs(root)
        return self.result