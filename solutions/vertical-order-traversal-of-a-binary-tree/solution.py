# Problem: Vertical Order Traversal of a Binary Tree
# URL: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = defaultdict(list)
        queue = deque([(root, 0, 0)]) # val, row, col
        result = []
        while queue:
            node, row, col = queue.popleft()
            nodes[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        for c in sorted(nodes.keys()):
            result.append([v for r, v in sorted(nodes[c])])
        return result
        