from collections import defaultdict

def num_trees(p):
    graph_dict = defaultdict(list)
    for i, p_i in enumerate(p):
        graph_dict[p_i].append(i)

    trees_counted = set()
    for tree_id in graph_dict:
        visited = set()
        queue = [tree_id]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend([neighbor for neighbor in graph_dict[node] if neighbor not in visited])
        trees_counted.add(tuple(sorted(list(visited))))

    return len(trees_counted)

n = int(input())
p = [int(x) for x in input().split()]
print(num_trees(p))
