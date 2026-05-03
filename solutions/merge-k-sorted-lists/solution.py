# Problem: Merge k Sorted Lists
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #O(Nlogk)
        # if not lists or len(lists)==0:
        #     return None
        # heap=[]
        # for i,node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap,(node.val,i,node))
        # temp=ListNode(0)
        # curr=temp
        # while heap:
        #     v,i,node=heapq.heappop(heap)
        #     curr.next=node
        #     curr=curr.next
        #     if node.next:
        #         heapq.heappush(heap,(node.next.val,i,node.next))
        # return temp.next

        #O(NlogN)
        heap = []
        # Put every node value into the min heap
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        # Build the sorted linked list from heap
        dummy = ListNode(0)
        curr = dummy

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return dummy.next