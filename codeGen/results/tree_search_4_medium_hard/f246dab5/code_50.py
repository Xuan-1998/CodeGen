def calculate_fare():
    n = int(input())  # number of trips

    dp = [[float('inf')] * (n + 1) for _ in range(10**9 + 1)]
    dp[0][0] = 0  # base case: no trips, no cost

    for i in range(n):
        t_i = int(input())  # time of trip i
        for j in range(i + 1, n + 1):  # consider all trips starting from this one onwards
            dp[t_i][j] = min(dp[max(0, t_i - 90)][j - 1] + 50,  # use a ticket for 90 minutes
                             dp[max(0, t_i - 1440)][j - 1] + 120,  # use a ticket for one day
                             dp[t_i - 1][j - 1] + 20)  # use a single ticket

    return sum(dp[10**9][i] for i in range(1, n + 1))

print(calculate_fare())
