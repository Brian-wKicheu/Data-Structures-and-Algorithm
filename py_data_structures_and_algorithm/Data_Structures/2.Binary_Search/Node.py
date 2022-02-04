class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild: 
                # means it's true we will initialize new node
                self.leftChild = Node(data)

            else:
                # we call insert method recursively
                self.leftChild.insert(data)

        # we have to do same for rightChild
        else:
            if not self.rightChild:
                self.rightChild = Node(data)

            else:
                self.rightChild.insert(data)

    # Method to get minimum value which is on leftChild
    def getMin(self):
        #we check if left child is none and if it's true we return data
        if self.leftChild is None:
            return self.data

        else:
            self.leftChild.getMin()

    # Methode to get maximum value which is on rightChild
    def getMax(self):
        if self.rightChild is None:
            return self.data

        else:
            self.rightChild.getMax()

    # Traverse-in-order method to sort given stack 
    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()

    def remove(self, data, parentNode):
        # We check if we have a data we need to remove
        if data < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self) # 'parentNode' is the 'self'

        elif data > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)

        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMin()
                self.rightChild.remove(self.data, self)

            elif parentNode.leftChild == self:
                # We check if it's not none
                if self.leftChild is not None:
                    # We're going to denote temporary node
                    tempNode = self.leftChild

                else:
                    tempNode = self.rightChild
                    
                # We assign it to the leftChild node
                parentNode.leftChild = tempNode

            elif parentNode.rightChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild

                else:
                    tempNode = self.rightChild

                # We keep updating the references
                parentNode.rightChild = tempNode