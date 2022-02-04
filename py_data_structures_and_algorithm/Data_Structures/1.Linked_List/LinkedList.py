# A linked list is a linear collection of data elements, whose order is not given by their physical placement
#  in memory. Instead, each element points to the next. It is a data structure consisting of a collection 
# of nodes which together represent a sequence.

from Node import Node;

class LinkedList(object):

    def __init__(self):
        # we going to create preference called 'head' which will reference the 1st Node. It's set to none bcoz
        # there are no nodes in our linked list
        self.head = None
        self.counter = 0

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

    # define if the node will start at beggining or end, in this case its start.
    def insertStart(self, data):

        self.counter += 1

        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # Let's set size of the linked list with a counter. Call counter as global and keep on increamenting
    def size(self):
        return self.counter

    def insertEnd(self, data):
        if self.head is None:
            self.insertStart(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            # if not we keep on iterating as follows
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):

        self.counter -=1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode

            else:
                self.head.remove(data, self.head)