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

    def recursiveInOrderTraversal(self):
        print("Recursive In Order Traversal")

        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                print(root.value)
                inOrderTraversal(root.right)

        inOrderTraversal(self.root)

    def recursivePreOrderTraversal(self):
        print("Recursive Pre Order Traversal")

        def preOrderTraversal(root):
            if root:
                print(root.value)
                preOrderTraversal(root.left)
                preOrderTraversal(root.right)

        preOrderTraversal(self.root)

    def recursivePostOrderTraversal(self):
        print("Recursive Post Order Traversal")

        def postOrderTraversal(root):
            if root:
                postOrderTraversal(root.left)
                postOrderTraversal(root.right)
                print(root.value)

        postOrderTraversal(self.root)


if __name__ == '__main__':
    binarySearchTree = BST()
    binarySearchTree.iterativeInsert(10)
    binarySearchTree.iterativeInsert(7)
    binarySearchTree.iterativeInsert(13)
    binarySearchTree.recursiveInOrderTraversal()
    binarySearchTree.recursivePreOrderTraversal()
    binarySearchTree.recursivePostOrderTraversal()
