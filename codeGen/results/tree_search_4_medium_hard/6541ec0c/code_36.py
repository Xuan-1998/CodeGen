import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[0] * (k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for child in range(1, n):
        for parent in range(child-1, -1, -1):
            if all(dp[ui][child-1] and all(dp[vi][child-1] for vi in [v for v in range(n) if (u, v) in edges]) for ui in range(parent+1, n)):
                dp[parent][child] = 1

    print("YES" if any(all(dp[i][j] for i in range(n)) for j in range(1, k+1)) else "NO")

if __name__ == "__main__":
    solve()
