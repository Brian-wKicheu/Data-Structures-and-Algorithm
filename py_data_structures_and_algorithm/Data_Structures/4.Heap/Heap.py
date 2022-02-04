class Heap(object):

    # static var for heap size
    HEAP_SIZE = 10
    
    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        # check if the heap is full
        if self.isFull():
            # & if its full print...
            print("Heap is full...")
            return

        # Increament current position
        self.currentPosition = self.currentPosition + 1
        # Insert current position
        self.heap[self.currentPosition] = item
        # We need to keep fixing our heap bcoz of the swapping to mantain the heap property
        self.fixUp(self.currentPosition)

    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False

    # We've to keep comparing items for parent and children and make swaps accordingly to mantain heap property
    def fixUp(self, index):
        # We need to calculate height of children with the height of the parent index
        parentIndex = int((index - 1)/2)

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            # we make necesary swaps
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            # we have to change the indexes inorder to iterate the tree
            index = parentIndex
            # set parent index to the next index
            parentIndex = int((index - 1)/2)

    def getMax(self):
        # we will the the root node with index of 0
        result = self.heap[0]
        self.currentPosition = self.currentPosition - 1 
        self.heap[0] = self.heap[self.currentPosition]
        # we remove obsolete values
        del self.heap[self.currentPosition+1]
        # we've to fix down with [0, -1]
        self.fixDown(0,-1)
        return result

    def fixDown(self, index, uptoIndex):
        if uptoIndex < 0:
            uptoIndex = self.currentPosition

        # iterate if the index is <= uptoIndex
        while index <= uptoIndex:
            # we calc the leftChild with half of the equition
            leftChild = 2*index + 1
            rightChild = 2*index + 2

            if leftChild <= uptoIndex:
                # we have to swap child. 1st initialize it to None
                childToSwap = None

                if rightChild > uptoIndex:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        # which is true we ...
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                    # because we've fineshed iteration

                index = childToSwap

            else:
                # break the loop
                break

    # perform O(N log N) sorting IN PLACE. It does not require additional memory, so we don't need to allocate any.
    def heapsort(self):
        # we've to construct the heap itself
        for i in range(0, self.currentPosition):
            temp = self.heap[0]
            # we get max element which is 0 and print it to console
            print("%d" % temp)
            # we've to swap with last element and after it's sorted we decrease the nodes(-i)
            self.heap[0] = self.heap[self.currentPosition - i]
            # we keep swapping elements
            self.heap[self.currentPosition - i] = temp
            # then we fix down
            self.fixDown(0, self.currentPosition-i-1)