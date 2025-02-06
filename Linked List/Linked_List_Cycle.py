# Link: https://leetcode.com/problems/linked-list-cycle/description/

# Using Hashset

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        while head:
            if head in dic:
                return True  
            else:
                dic[head] = head.next
                head = head.next

        return False  



# Two Pointer Approach (Floyd's Tortoise and Hare)

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> dict:
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next

            if s == f:
                return True

        return False

# Create a linked list: 1 -> 2 -> 3 -> None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node3

# Call the method
solution = Solution()
result = solution.hasCycle(node1)

print(result)