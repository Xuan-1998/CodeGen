def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (k+1) for _ in range(n)]
    prev = [[0] * (k+1) for _ in range(n)]
    
    for i in range(k):
        prev[i][0] = 'R' if i % 3 == 0 else 'G' if i % 3 == 1 else 'B'
    
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(min(i+1, k+1), -1, -1):
            if s[i-1] != prev[i-1][j-1]:
                dp[i][j] = min(dp[i-1][j-1]+1, j)
            else:
                dp[i][j] = dp[i-1][j]
            prev[i][j] = s[i-1]
    
    print(dp[-1][-1])
