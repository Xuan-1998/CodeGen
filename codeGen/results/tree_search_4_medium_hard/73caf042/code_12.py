def total_diamonds(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            sum_even = sum(int(digit) for digit in str(i + j))
            sum_odd = sum(int(digit) for digit in str(i + j)) - sum_even
            dp[i][j] = abs(sum_even - sum_odd) + (i > 0 and j > 0 and dp[i-1][j-1])
    
    return dp[N][N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(total_diamonds(N))
