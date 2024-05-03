def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(i + 1):
                if arr[j] > 0:
                    dp[i][j] = dp[i-1][j] or (arr[j] - 1) % 2 == 0 and dp[i-1][j-1]
        
        print("YES" if dp[n][0] else "NO")

solve()
