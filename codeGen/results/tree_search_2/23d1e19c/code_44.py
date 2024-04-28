import sys
from collections import deque, defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [float('inf')] * (n + 1)
    dp[path[0]] = 0

    for i in range(1, k):
        j = path[i]
        dp[j] = min(dp[j], dp[path[i - 1]] + 1)

    max_recomputations = 0
    current_recomputations = 0
    for i in range(k, n + 1):
        if graph[i]:
            j = min(graph[i])
            dp[j] = min(dp[j], dp[i] + 1)
            current_recomputations += 1
            max_recomputations = max(max_recomputations, current_recomputations)

    print(min(dp), max_recomputations)

if __name__ == "__main__":
    main()
