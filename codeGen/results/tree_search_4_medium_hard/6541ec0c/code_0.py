import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[False] * (k+1) for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(min(k, i-1), -1, -1):
            if all(values[edges[x][0]] ^ values[edges[x][1]] == values[i] for x in range(i)):
                dp[i][j] = True
                break

    print("YES" if any(dp[i][k] for i in range(2, n+1)) else "NO")

if __name__ == "__main__":
    solve()
