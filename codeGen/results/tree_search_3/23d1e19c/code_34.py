from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))

    dp = [float('inf')] * (n + 1)
    dp[s] = 0

    for i in range(n):
        if i == s:
            continue
        for j in range(i, t+1):
            if has_edge(j, i):
                dp[i] = min(dp[i], dp[j] + (t - i))

    print(min(dp), max(dp))

def has_edge(u, v):
    return u in graph[v]

if __name__ == "__main__":
    solve()
