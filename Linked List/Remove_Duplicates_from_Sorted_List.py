# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Solution Article: https://vishwanathts.hashnode.dev/efficient-solution-to-remove-duplicates-from-sorted-linked-list-in-python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next

        return head