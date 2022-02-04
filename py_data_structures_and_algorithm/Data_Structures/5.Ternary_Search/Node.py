class Node(object):

    def __init__(self, character):
        self.character = character
        # The leftNode is the Lesser, middleNode = Equals to, and rightNode = Greater 
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None