from Node import Node;

class TST(object):

    def __init__(self):
        self.rootNode = None

    # Define PUT method
    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    # Define putItem method called above
    def putItem(self, node, key, value, index):
        # c is the character we'll instantiate with
        c = key[index]

        if node == None:
            # We instatiate with the character
            node = Node(c)

        if c < node.character:
            # It becomes a prediccessor
            # we go to the left and call putItem method recursively
            node.leftNode = self.putItem(node.leftNode, key, value, index)

        elif c > node.character:
            # it means it's a successor
            node.rightNode = self.putItem(node.rightNode, key, value, index)

        # We check for the middleNode We know it's smaller but we make it efficient by checking for length
        elif index < len(key)-1:
            # Increament the index here
            node.middleNode = self.putItem(node.middleNode, key, value, index +1)

        # if all conditions above are None we instert the value 
        else:
            node.value = value

        return node

    # def get method
    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        # check if
        if node == None:
            return None

        return node.value

    def getItem(self, node, key, index):
        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftNode, key, index)

        elif c > node.character:
            return self.getItem(node.rightNode, key, index)

        elif index < len(key) -1:
            return self.getItem(node.middleNode, key, index +1)

        else:
            return node