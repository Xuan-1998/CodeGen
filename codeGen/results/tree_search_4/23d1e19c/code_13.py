===BEGIN CODE===
import sys
from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, edges, k, path

def main():
    n, m, edges, k, path = read_input()
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    dp = [[n+1] * (n+1) for _ in range(k+1)]
    prev_vertex = 0
    for i in range(1, k+1):
        if path[i-1] == path[i]:
            continue
        min_recompute = n+1
        max_recompute = 0
        for j in graph[path[i-1]]:
            if j != path[i]:
                min_recompute = min(min_recompute, dp[prev_vertex][j])
                max_recompute = max(max_recompute, dp[prev_vertex][j])
        dp[i][path[i]] = min_recompute + 1
        prev_vertex = i

    print(dp[-1][-1], end=' ')

    min_max_recompute = n+1
    for j in graph[path[-2]]:
        if j != path[-1]:
            min_max_recompute = min(min_max_recompute, dp[-2][j])
    print(min_max_recompute + 1)

if __name__ == "__main__":
    main()

===END CODE===
