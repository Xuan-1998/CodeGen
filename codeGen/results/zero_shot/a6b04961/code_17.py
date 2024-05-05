import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [0] * (n + 1)
    max_beauty = 0

    for i in range(2, n + 1):
        max_spines = 0
        for j in range(i - 1, 1, -1):
            max_spines = max(max_spines, dp[j-1] * (n - j))
        dp[i] = max_spines
        max_beauty = max(max_beauty, dp[i])

    print(max_beauty)

if __name__ == "__main__":
    solve()
