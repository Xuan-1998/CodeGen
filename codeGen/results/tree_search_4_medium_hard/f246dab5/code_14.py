n = int(input())  # number of trips

dp = [0] * (n + 1)  # dynamic programming array

for i in range(1, n+1):
    t_i = int(input())  # time of trip i
    if t_i > 1440:  # one day ticket
        dp[i] = dp[i-1] + 120
    elif t_i > 90:
        dp[i] = min(dp[i-1], dp[i-2]) + 50
    else:
        dp[i] = min(dp[i-1], dp[i-2]) + 20

print(*dp[1:], sep='\n')  # print the minimum fare for each trip
