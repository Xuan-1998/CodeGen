import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    fixed_path = list(map(int, input().split()))
    for u, v in (map(int, input().split()) for _ in range(m)):
        graph[u].append(v)

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i == fixed_path[i - 1]:
            dp[i] = min(dp[i - 1], 1) if i > 1 else 0
        else:
            dp[i] = min(dp[i - 1], 1) + 1

    print(min(dp), max(dp))

if __name__ == "__main__":
    solve()
