# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
            

        left.next = left.next.next
        return dummy.next

# Helper functions
def create_linked_list(elements):
    """Creates a linked list from a list of elements."""
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints a linked list in a readable format."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("->".join(map(str, result)))

# Test the solution
elements = [1, 2, 3, 4, 5]  # Elements of the linked list
n = 2  # Position from the end to remove

# Create the linked list
head = create_linked_list(elements)


# Apply the solution
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)

# Print the updated linked list
print("Updated Linked List:")
print_linked_list(new_head)
