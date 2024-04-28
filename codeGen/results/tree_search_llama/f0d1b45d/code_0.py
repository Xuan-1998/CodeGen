def find_trees(p):
    n = int(input())
    trees = {}
    for i, p_i in enumerate(map(int, input().split()), 1):
        tree_id = min(trees.get(p_i, set()), key=len)
        trees[tree_id].add(i)

    return len(trees)

print(find_trees(input()))
