from Node import Node;

class BalancedTree(object):

    # constractor
    def __init__(self):
        self.rootNode = None

    # method with data we will insert
    def insert(self, data):
        parentNode = self.rootNode

        if self.rootNode == None:
            # it means the binary search tree is empty
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            # call insert method in the Node class. Import the class
            parentNode = self.rootNode.insert(data, self.rootNode)

        # we call rebalance tree method that we will implement below
        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        # we must set the balance by getting the height that's why we must create balance method
        self.setBalance(parentNode)

        # after you setBalance and height now here set rotations
        if parentNode.balance < -1:
            if self.height(parentNode.leftChild.leftChild) >= self.height(parentNode.leftChild.rightChild):
                # if that's true do below and create method
                parentNode = self.rotateRight(parentNode)
            else:
                # if it ain't true rotate to the left-right and implement the method
                parentNode = self.rotateLeftRight(parentNode)

        # check if parentNode is balanced is > +1
        elif parentNode.balance > 1:
            if self.height(parentNode.rightChild.rightChild) >= self.height(parentNode.rightChild.leftChild):
                # if that's true make left rotation
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)

        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)

        else:
            self.rootNode = parentNode

    def setBalance(self, node):
        node.balance = (self.height(node.rightChild) - self.height(node.leftChild))

    # getting the height of the node with below iterating formulas
    def height(self, node):
        if node == None:
            return -1 
        else:
            return 1+ max(self.height(node.leftChild), self.height(node.rightChild))

    # below are rotations (You can google because it is specified how to make rotations in AVL Tree)
    def rotateLeftRight(self, node):
        print("Rotate left right...")
        node.leftChild = self.rotateLeft(node.leftChild)
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        print("Rotate right left...")
        node.rightChild = self.rotateRight(node.rightChild)
        return self.rotateLeft(node)

    def rotateLeft(self, node):
        print("Rotate left...")
        # let's create temporary variable
        b = node.rightChild
        b.parentNode = node.parentNode
        # set it to the leftChild
        node.rightChild = b.leftChild
        if node.rightChild is not None:
            node.rightChild.parentNode = node

        b.leftChild = node
        node.parentNode = b

        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b
            else:
                b.parentNode.leftChild = b

        # after all these operation we must set the balance for node and b itself
        self.setBalance(node)
        self.setBalance(b)

        return b

    def rotateRight(self, node):
        print("Rotate right...")
        b = node.leftChild
        b.parentNode = node.parentNode
        node.leftChild  = b.rightChild
        if node.leftChild is not None:
            node.leftChild.parentNode = node

        b.rightChild = node
        node.parentNode = b

        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b
            else:
                b.parentNode.leftChild = b

        self.setBalance(node)
        self.setBalance(b)

        return b

    # call traverse from Node.py
    def traverseInOrder(self):
        self.rootNode.traverseInOrder()