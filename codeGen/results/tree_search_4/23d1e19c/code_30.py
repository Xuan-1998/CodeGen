import sys

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [0] * (n + 1)
    max_recompute = 0
    min_recompute = sys.maxsize

    for i in range(k):
        if i == 0:
            continue
        dp[path[i]] = max(dp[path[i-1]], dp[path[i-1]] + 1)
        recompute = dp[path[i-1]]
        max_recompute = max(max_recompute, recompute)
        min_recompute = min(min_recompute, recompute)

    print(min_recompute, max_recompute)

if __name__ == "__main__":
    main()
