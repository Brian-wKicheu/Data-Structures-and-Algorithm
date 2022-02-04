from TST import TST;

tree = TST()

tree.put("apple", 100)
tree.put("orange", 200)

print(tree.get("apple"))
print(tree.get("apble"))
print(tree.get("orange"))
print(tree.get("oranje"))