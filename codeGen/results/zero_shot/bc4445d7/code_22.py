def solve():
    T, n, edges, m, primes = read_input()
    for _ in range(T):
        parent_count = [0] * (n + 1)
        child_count = [0] * (n + 1)
        edge_count = [0] * (n + 1)
        root = max(range(2, n + 1), key=lambda x: parent_count[x])
        for u, v in edges:
            parent_count[u] += 1
            child_count[v] += 1
            edge_count[u] += 1
        total_ones = 1
        for i in range(n):
            if parent_count[i + 1]:
                total_ones += 1
                root = i
                break
        index = sum(parent_count[:root]) - 1
        for u, v in edges:
            if u == root:
                edge_count[v] -= 1
                child_count[u] -= 1
            elif v == root:
                edge_count[u] -= 1
                parent_count[v] += 1
        total_distribution_index = sum(sum(parent_count[:i]) for i in range(2, n + 1))
        print(total_distribution_index % (10**9 + 7))

solve()
