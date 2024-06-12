class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position.")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            temp = temp.next
            if temp == self.head:
                print("Position exceeds the length of the list.")
                return
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        if not self.head:
            print("Circular linked list is empty.")
            return
        temp = self.head
        if temp.data == key:
            last = self.head
            while last.next != self.head:
                last = last.next
            if self.head == self.head.next:
                self.head = None
            else:
                last.next = self.head.next
                self.head = self.head.next
            return
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            if temp.data == key:
                prev.next = temp.next
                return
        print("Node with key {} not found.".format(key))

    def search(self, key):
        if not self.head:
            print("Circular linked list is empty.")
            return
        temp = self.head
        found = False
        while True:
            if temp.data == key:
                print("Node with key {} found.".format(key))
                found = True
                break
            temp = temp.next
            if temp == self.head:
                break
        if not found:
            print("Node with key {} not found.".format(key))

    def display(self):
        if not self.head:
            print("Circular linked list is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                print("...")
                break

if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.insert_at_beginning(9)
    circular_linked_list.insert_at_beginning(7)
    circular_linked_list.insert_at_beginning(3)
    circular_linked_list.display()

    circular_linked_list.insert_at_position(5, 2)
    circular_linked_list.insert_at_position(11, 4)
    circular_linked_list.display()

    circular_linked_list.search(5)

    circular_linked_list.delete_node(7)
    circular_linked_list.display()
