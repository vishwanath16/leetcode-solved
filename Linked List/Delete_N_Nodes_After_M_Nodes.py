# Link: https://leetcode.com/problems/delete-n-nodes-after-m-nodes/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_nodes(head, m, n):
    pre = head
    while pre:
        for _ in range(m - 1):
            if pre:
                pre = pre.next
        if pre is None:
            return head
        cur = pre
        for _ in range(n):
            if cur:
                cur = cur.next
        pre.next = None if cur is None else cur.next
        pre = pre.next
    return head

# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Example usage
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)



    M, N = 2, 3
    head = delete_nodes(head, M, N)
    print_list(head)  # Expected: 1 -> 2 -> 5 -> 6 -> 9 -> 10