class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False