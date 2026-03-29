    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1

    for u, v in edges:
        union(u, v)

    connected_components = {}
    for i in range(1, n):
        parent[i] = find(i)
        if parent[i] not in connected_components:
            connected_components[parent[i]] = [i]
        else:
            connected_components[parent[i]].append(i)

    max_distribution_index = 0
    for component in connected_components.values():
        total_edges = len(component) - 1
        total_sum = 0
        for i in range(len(component) - 1):
            u, v = component[i], component[i+1]
            total_sum += (product // ((component[-1] - u + 1) * (v - u))) ** ((component[-1] - u + 1) * (v - u))
        max_distribution_index = (max_distribution_index + total_edges * total_sum) % (10**9 + 7)

    print(max_distribution_index)
