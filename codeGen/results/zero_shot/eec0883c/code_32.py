def solve():
    n = int(input())
    w = list(map(int, input().split()))
    tree_edges = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        tree_edges.append((u, v, c))

    max_gasoline = 0

    def dfs(city, parent_city, remaining_gasoline):
        nonlocal max_gasoline
        if city == 1:  # Start from the first city
            max_gasoline = max(max_gasoline, remaining_gasoline)
        else:
            for neighbor_city, edge_c in tree_edges:
                if neighbor_city == city and edge_c < remaining_gasoline:
                    dfs(neighbor_city, city, remaining_gasoline - edge_c)

    dfs(1, 0, w[0])
    print(max_gasoline)

if __name__ == "__main__":
    solve()
