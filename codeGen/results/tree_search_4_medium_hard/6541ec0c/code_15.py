def dfs(node_id, memo):
    if node_id not in memo:
        children = []
        for child in edges[node_id]:
            if child not in memo:
                is_unique_xor, xor_value = dfs(child, memo)
                memo[node_id] = (is_unique_xor and all(xor_value == memo[child][1] for child in edges[node_id]), xor_value ^ memo[child][1])
            else:
                memo[node_id] = memo[child]
            children.append((child, is_unique_xor, memo[node_id]))

        if len(children) > 0:
            is_unique_xor = all(child[0] for child in children)
            memo[node_id] = (is_unique_xor, memo[children[0][2]][1])
        else:
            memo[node_id] = (True, 0)

    return memo[node_id]

n, k = map(int, input().split())
values = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

memo = {}
is_unique_xor = dfs(0, memo)[0]
print("YES" if is_unique_xor else "NO")
