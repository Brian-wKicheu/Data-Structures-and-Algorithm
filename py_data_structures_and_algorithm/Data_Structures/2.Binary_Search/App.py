# For passing DS

from BinarySearchTree import BST;

bst = BST()

print("--- Prints the entire insert in ascending order ---")
bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)
# Let's order the nodes/values
bst.traverseInOrder()

print("--- Testing Remove Method---")
# Let's try to remove
bst.remove(10)
bst.traverseInOrder()

# print("--- Testing getMax Method---")
# print(bst.getMax())

print("--- Testing getMin Method---")
print(bst.getMin())