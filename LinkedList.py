class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # O(n) time | O(1) space
    def iterativeInsertAtEnd(self, valueToInsert):
        if self.head is None:
            self.head = Node(valueToInsert)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(valueToInsert)

    def insertAtBeginning(self, valueToInsert):
        if self.head is None:
            self.head = Node(valueToInsert)
        else:
            newHead = Node(valueToInsert)
            newHead.next = self.head
            self.head = newHead

    # O(n) time | O(1) space
    def iterativePrint(self):
        print("Linked list iterative print")
        current = self.head
        while current:
            print(current.value)
            current = current.next

    # O(n) time | O(1) space
    def iterativeReverse(self):
        prev, current = None, self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    # O(n) time | O(n) space
    def recursiveReverse(self):
        print('Linked list recursive reverse')

        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                next = curr.next
                curr.next = prev
                return reverse(next, curr)

        self.head = reverse(self.head, None)


if __name__ == '__main__':
    List = LinkedList()
    List.iterativeInsertAtEnd(10)
    List.iterativeInsertAtEnd(11)
    List.iterativePrint()
    List.recursiveReverse()
    List.iterativePrint()
