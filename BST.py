class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def iterativeInsert(self, valueToInsert):
        if self.root is None:
            self.root = Node(valueToInsert)
            return
        parentNode = None
        currentNode = self.root
        while currentNode:
            if valueToInsert >= currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif valueToInsert < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
        if parentNode.value < valueToInsert:
            parentNode.right = Node(valueToInsert)
        else:
            parentNode.left = Node(valueToInsert)


if __name__ == '__main__':
    binarySearchTree = BST()
    binarySearchTree.iterativeInsert(10)
    binarySearchTree.iterativeInsert(7)
    binarySearchTree.iterativeInsert(13)
