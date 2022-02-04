def dfs(node):

    node.visited = True
    # print our node here
    print("%s ->" % node.name)

    # n(number) denotes all.
    for n in node.adjacentList:
        if not n.visited:
            dfs(n)