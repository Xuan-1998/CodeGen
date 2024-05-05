from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        for j in graph[i]:
            if dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1

    print(min(dp[1:]))  # Minimum number of reversed edges
    print(*[i for i, d in enumerate(dp) if d == min(dp)], sep=' ')  # Capital city indices

if __name__ == '__main__':
    solve()
