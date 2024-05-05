import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize base cases
    for i in range(N+1):
        dp[i][0] = i
    
    for i in range(1, N+1):
        for j in range(min(i, N-i)+1):
            if j == 0:
                dp[i][j] = i
            elif j == N-i:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][N-j]) / 2
    
    # Calculate expected number of non-zero carries
    total_carries = sum(dp[N][i] for i in range(N+1))
    
    print(total_carries / (N*(N+1)//2))
