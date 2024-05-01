from collections import defaultdict

def solve(n, m, graph, k, s_to_t):
    dp = [[float('inf'), 0] for _ in range(n)]
    memo = {}

    def f(u):
        if u not in memo:
            min_rec = float('inf')
            max_rec = 0
            for p in s_to_t:
                if graph[u][p]:
                    rec, dp_u_p = f(p)
                    min_rec = min(min_rec, 1 + dp_u_p[0])
                    max_rec = max(max_rec, 1 + dp_u_p[1])
            memo[u] = (min_rec, max_rec)
        return memo[u]

    for u in range(n):
        if u not in s_to_t:
            dp[u][u] = (0, 0)

    min_rec = f(s_to_t[0])[0]
    max_rec = f(s_to_t[0])[1]

    print(min_rec, max_rec)


# Example usage
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
s_to_t = list(map(int, input().split()))
solve(n, m, graph, k, s_to_t)
