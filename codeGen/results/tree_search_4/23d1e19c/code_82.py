from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    p = list(map(int, input().split()))
    memo = {}

    def dp(u):
        if u == p[-1]:
            return 0, 0
        if u in memo:
            return memo[u]

        min_recomputation = max_recomputation = float('inf')
        for v in graph[u]:
            if v > u:
                min_recomputation, max_recomputation = dp(v)
                break

        if u == p[0]:
            min_recomputation -= 1
            max_recomputation += 1
        else:
            prev_u = p[p.index(u) - 1]
            min_recomputation, max_recomputation = dp(prev_u)
            min_recomputation -= 1
            max_recomputation += 1

        memo[u] = (min_recomputation, max_recomputation)
        return memo[u]

    print(dp(p[0]))

if __name__ == "__main__":
    solve()
