class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def iterativeInsertAtEnd(self, valueToInsert):
        if self.head is None:
            self.head = Node(valueToInsert)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(valueToInsert)

    def iterativePrint(self):
        print("Linked list iterative print")
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    List = LinkedList()
    List.iterativeInsertAtEnd(10)
    List.iterativeInsertAtEnd(11)
    List.iterativePrint()