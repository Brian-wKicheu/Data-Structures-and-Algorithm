from BalancedTree import BalancedTree;

tree = BalancedTree()

# when you insert this we expect right-rotation and a left-rotation
# tree.insert(4)
# tree.insert(6)
# tree.insert(5)

tree.insert(4)
tree.insert(2)
tree.insert(3)

tree.traverseInOrder()