def solve():
    n = 2**30
    dp = [[False] * n for _ in range(n)]
    
    # Base case: no path to self
    for i in range(n):
        dp[i][i] = False
    
    q = int(input())
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        for w in range(n):
            if (u & w) == w:
                dp[u][v] = all(dp[w][i] and (w & i) == i for i in range(v + 1))
        
        print("YES" if dp[u][v] else "NO")

if __name__ == "__main__":
    solve()
