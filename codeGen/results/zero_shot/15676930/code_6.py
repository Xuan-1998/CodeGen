def solve():
    n = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))

    dp = [[0] * 3 for _ in range(n + 1)]
    
    # Base case
    for i in range(3):
        dp[1][i] = [a_values[i], b_values[i], c_values[i]][i]
    
    # Fill up the dp table
    for i in range(2, n + 1):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i - 1][1], dp[i - 1][2]) + a_values[i]
            elif j == 1:
                dp[i][j] = max(max(dp[i - 1][:2]), dp[i - 1][2]) + b_values[i]
            else:
                dp[i][j] = max(max(dp[i - 1][:2]), dp[i - 1][1]) + c_values[i]
    
    return max(dp[n])
