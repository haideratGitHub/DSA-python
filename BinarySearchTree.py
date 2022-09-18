class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
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

    def recursiveInsert(self, valueToInsert):

        def insert(curr, parent, value):
            if curr is None:
                if parent.value < value:
                    parent.right = Node(value)
                else:
                    parent.left = Node(value)
            else:
                if curr.value < value:
                    insert(curr.right, curr, value)
                elif curr.value > value:
                    insert(curr.left, curr, value)

        if self.root is None:
            self.root = Node(valueToInsert)
        else:
            insert(self.root, None, valueToInsert)

    def recursiveInOrderTraversal(self):
        print("Recursive In Order Traversal")

        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                print(root.value)
                inOrderTraversal(root.right)

        inOrderTraversal(self.root)

    def iterativeInOrderTraversal(self):
        print("Iterative In Order Traversal")
        stack = []
        current = self.root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value)
                current = current.right
            else:
                break

    def recursivePreOrderTraversal(self):
        print("Recursive Pre Order Traversal")

        def preOrderTraversal(root):
            if root:
                print(root.value)
                preOrderTraversal(root.left)
                preOrderTraversal(root.right)

        preOrderTraversal(self.root)

    def iterativePreOrderTraversal(self):
        print("Iterative Pre Order Traversal")
        current = self.root
        stack = []
        stack.append(current)
        while stack:
            current = stack.pop()
            print(current.value)

            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    def recursivePostOrderTraversal(self):
        print("Recursive Post Order Traversal")

        def postOrderTraversal(root):
            if root:
                postOrderTraversal(root.left)
                postOrderTraversal(root.right)
                print(root.value)

        postOrderTraversal(self.root)

    def iterativePostOrderTraversal(self):
        pass

    def iterativeContains(self, value):
        print(f'Finding {value} in BST iteratively')
        current = self.root
        if current.value == value:
            return True
        while current:
            if current.value < value:
                current = current.right
            elif current.value > value:
                current = current.left
            else:
                return True
        return False

    # leetcode 98
    def validateBST(self):
        def dfs(root, left, right):
            if not root:
                return True
            else:
                if not (root.value > left and root.value < right):
                    return False
                return dfs(root.left, left, root.value) and dfs(root.right, root.value, right)

        return dfs(self.root, float('-inf'), float('inf'))

    # leetcode 235
    def lowestCommonAncestor(self, p, q):
        print("Finding lowest common ancestor")
        current = self.root
        while current:
            if p > current.value and q > current.value:
                current = current.right
            elif p < current.value and q < current.value:
                current = current.left
            else:
                return current.value


if __name__ == '__main__':
    Bst = BinarySearchTree()
    Bst.iterativeInsert(10)
    Bst.iterativeInsert(7)
    Bst.iterativeInsert(13)
    Bst.recursiveInsert(14)
    Bst.recursiveInsert(6)

    Bst.recursivePostOrderTraversal()
    Bst.iterativePostOrderTraversal()
    print(Bst.lowestCommonAncestor(6, 14))
    print(Bst.validateBST())
    print(Bst.iterativeContains(14))
