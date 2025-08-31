# Link: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For printing linked list
    def __repr__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return str(result)

# Utility to convert list to linked list
def list_to_linkedlist(items: List[int]):
    dummy = ListNode()
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

# Utility to convert linked list to list
def linkedlist_to_list(node) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next

# Example usage
if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # Should print [7, 0, 8] after you implement the logic
