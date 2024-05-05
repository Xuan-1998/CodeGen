def send_sequence():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(i + 1):
                if b[j - 1] <= i:
                    if j == 0 or b[j - 1] != b[i]:
                        dp[i][j] = any(dp[k][l] and (i - k) >= s and (k - l) >= len(s) for k in range(i) for l in range(k) for s in range(1, i - k + 1))
                    else:
                        if j == i or b[j] != b[i]:
                            dp[i][j] = any(dp[k][l] and (i - k) >= s and (k - l) >= len(s) for k in range(i) for l in range(k) for s in range(1, i - k + 1))
        
        print("YES" if dp[n - 1][n] else "NO")

send_sequence()
