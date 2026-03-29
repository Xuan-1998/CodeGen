import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        u, v = map(int, input().split())
        for j in range(k - 1, 0, -1):
            if dp[u][j - 1]:
                dp[i][j] = (dp[v][j - 1]) or (all(values[:u] + [values[u]]) == values[u])
            elif dp[v][j - 1]:
                dp[i][j] = all(x ^ values[0] for x in values[1:])
    
    print("YES" if dp[0][k] else "NO")

if __name__ == "__main__":
    solve()
