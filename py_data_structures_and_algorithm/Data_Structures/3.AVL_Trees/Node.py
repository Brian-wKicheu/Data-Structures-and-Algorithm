class Node:

    # def constructor.
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        # we need a balance number
        self.balance = 0

    def insert(self, data, parentNode):
        if data < self.data:
            # we go to the leftChild
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            # else is not null
            else:
                # we call insert method the data with parent
                self.leftChild.insert(data, parentNode)

        else:
            # we move to the right child
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                # we call it recursively
                self.rightChild.insert(data, parentNode)

        return parentNode

    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInOrder()

    # The value greater than root node goes to the right node
    def getMax(self):
        if not self.rightChild:
            return self.data

        else:
            return self.rightChild.getMax()

    # The value lesser than root node goes to left Node
    def getMin(self):
        if not self.leftChild:
            return self.data

        else:
            return self.leftChild.getMin()