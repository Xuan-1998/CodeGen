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
    for i in range(n):
        if i == 0:
            dp[i] = 1
        else:
            if i == path[k - 1]:
                break
            max_recomputation = 0
            for v in graph[path[k - 1]]:
                if v != i and v not in path[:k]:
                    max_recomputation = max(max_recomputation, dp[v])
            dp[i] = 1 + max_recomputation

    print(min(dp[1:]), max(dp[1:]))

if __name__ == "__main__":
    main()
