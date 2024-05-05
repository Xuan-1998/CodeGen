def min_operations():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))

    def dfs(i, value, ops):
        if i > 0:
            ops += max(0, (ranges[i][1] - value) + (value - ranges[i][0]))
            if parent[i-1]:
                return ops + dfs(parent[i-1], value+1, 0)
            return ops
        return ops

    print(dfs(n, 0, 0))

min_operations()
