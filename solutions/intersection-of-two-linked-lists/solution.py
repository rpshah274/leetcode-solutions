# Problem: Intersection of Two Linked Lists
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A=headA
        B=headB
        while A!=B:
            if A:
                A=A.next
            else:
                A=headB
            if B:
                B=B.next
            else:
                B=headA
        return A
        