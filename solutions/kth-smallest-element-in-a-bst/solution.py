# Problem: Kth Smallest Element in a BST
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.inord(root,k)
        return self.res

    def inord(self,node,k):
        if not node:
            return None
        self.inord(node.left,k)
        self.k-=1
        if self.k==0:
            self.res = node.val
            return
        self.inord(node.right,k)
