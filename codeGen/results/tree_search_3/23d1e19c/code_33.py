import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t = map(int, input().split())
    path_length = int(input())

    dp = [0] * (n + 1)
    min_dp = [float('inf')] * (n + 1)

    for i in range(path_length - 1):
        j = list(graph)[path_length - 1 - i]
        if i == 0:
            dp[0] = path_length - 1
            min_dp[0] = path_length - 1
        else:
            dp[j] = max(dp[i])
            min_dp[j] = min(min_dp[i]) + (t - i)

    for vertex in range(s, t):
        if graph[vertex]:
            dp[vertex] = max(dp[x] for x in graph[vertex])
            min_dp[vertex] = min(min_dp[x] + 1 for x in graph[vertex])

    print(min_dp[t], dp[t])

if __name__ == "__main__":
    main()
