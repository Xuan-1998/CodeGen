cost = 20
max_j = int(10**5)  # Assuming at most 10^5 trips
max_k = int(10**5)//90
n = int(input())  # Number of trips

dp = [[[cost for _ in range(max_k+1)] for _ in range(max_j+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0][0] = cost

for i in range(1, n+1):
    for j in range(max_j+1):
        for k in range(max_k+1):
            # Consider using one more ticket of type A (1-trip)
            if i <= t_i and dp[i-1][j+1][k] + 20 < dp[i][j][k]:
                dp[i][j][k] = dp[i-1][j+1][k] + 20
            # Consider using one more ticket of type B (90-minute)
            if i <= t_i and k < 10**5//90 and dp[i-1][j][k+1] + 50 < dp[i][j][k]:
                dp[i][j][k] = dp[i-1][j][k+1] + 50

for i in range(1, n+1):
    for j in range(max_j+1):
        for k in range(max_k+1):
            print(dp[i][j][k])
