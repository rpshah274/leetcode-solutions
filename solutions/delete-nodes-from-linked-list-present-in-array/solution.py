# Problem: Delete Nodes From Linked List Present in Array
# URL: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hashset=set(nums)
        dummy=ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val in hashset:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
