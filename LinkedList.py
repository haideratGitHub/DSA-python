class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def iterativePrint(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    List = LinkedList()
