class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    # let's create a remove node method that saves as previous
    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            # inorder to avoid obsolete preferences we need to get rid of the preferences (data & nextNode)
            del self.data
            del self.nextNode

        # else we need to check if next node aint NULL
        else:
            if self.nextNode is not None:
                # we remove method recursively
                self.nextNode.remove(data, self)