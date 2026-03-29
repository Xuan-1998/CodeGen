def send_sequence_over_network():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, min(i, n) + 1):
                if j == 1:
                    dp[i][j] = True
                elif dp[j - 1][i - 1] and a[i - 1] == b[i]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        
        print("YES" if dp[n][n] else "NO")

send_sequence_over_network()
