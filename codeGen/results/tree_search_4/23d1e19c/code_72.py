import sys

def main():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(m):
        u, v = path[i], path[i+1]
        if v not in graph[u]:
            dp[v] = min(dp[v], dp[u]+1)

    res = []
    for i in range(n):
        res.append(max(res) if res else 0)
    print(*res)

if __name__ == "__main__":
    main()
