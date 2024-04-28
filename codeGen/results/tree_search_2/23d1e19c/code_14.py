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

    s, t = map(int, input().split())
    k = int(input())
    path = list(map(int, input().split()))

    dp = [[sys.maxsize, 0] for _ in range(n+1)]
    dp[t][0] = [0, 0]

    for i in range(k-1, -1, -1):
        u = path[i]
        v = path[i+1]
        for j in range(2):
            if dp[v][j] > dp[u][j]:
                dp[v][j] = dp[u][j]
            else:
                dp[v][j] += 1

    print(min(dp[s]), max(dp[s]))

if __name__ == "__main__":
    main()
