from Node import Node
import DFS

# Create nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

# Set nodes
node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)
#           A
#         /   \
#        B     C
#       /       
#      D
#     /
#    E

# call dfs function parsing node1 as root node
DFS.dfs(node1)