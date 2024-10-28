class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  


    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(None)


l1 = LinkedList()

l1.append(1)
l1.append(2)
l1.append(3)

l1.display()