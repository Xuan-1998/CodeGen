def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        scores = list(map(int, input().split()))
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(min(i - 1, k)):
                if j < z:
                    # no move
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j] + scores[i-1])
                else:
                    # one or more moves to the left, so consider right move
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j+1] + scores[i-1])
        
        print(max(dp[n]))
