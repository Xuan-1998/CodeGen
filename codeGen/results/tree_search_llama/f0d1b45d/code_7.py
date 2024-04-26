    n = int(input())
    parent = {}
    traversals = []
    for i in range(1, n+1):
        pi = int(input())  # input for Ball i's most distant relative living on the same tree
        if parent.get(pi) is None:  # if this is a new vertex (root)
            parent[pi] = None  # set its parent to None
        else:
            parent[pi] = pi-1  # otherwise, it's a child of the previous vertex
    traversals = [inorder_traversal(i) for i in range(1, n+1)]
    print(count_trees(traversals))

