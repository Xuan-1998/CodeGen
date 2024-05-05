def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for i in range(n-1):
        u, v = map(int, input().split())
        parent[v] = u

    dp = [[False] * k for _ in range(n)]
    dp[0][0] = True

    for i in range(1, n):
        dp[i][0] = True
        for j in range(1, min(i+1, k)):
            dp[i][j] = dp[find(i)][j-1]
            if dp[i][j]:
                break
    
    print("YES" if dp[n-1][k-1] else "NO")

if __name__ == "__main__":
    solve()
