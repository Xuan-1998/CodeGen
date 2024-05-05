def canSendOverNetwork():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True
        prev_val = -1
        n -= 1
        for i in range(1, n + 1):
            if b[i] == prev_val:
                dp[i][i] = dp[i-1][i]
            else:
                for j in range(i+1):
                    if dp[j][i-j]:
                        dp[i][j] = True
                        break
            prev_val = b[i]
        print('YES' if any(dp[i][n-i] for i in range(n + 1)) else 'NO')

canSendOverNetwork()
