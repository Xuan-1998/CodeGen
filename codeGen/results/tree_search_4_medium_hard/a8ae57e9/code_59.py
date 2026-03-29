def max_earnings(n, k, p):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if p[i - 1][0] > j:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = sum(p[:i]) if dp[i - 1][j - 1] == 0 else max(dp[i - 1][j], dp[i][j - 1])

    accepted_requests, total_earnings = 0, dp[n][k]
    for i in range(n):
        if p[i][1] > k:
            break
        if dp[i][p[i][1]] == total_earnings:
            accepted_requests += 1
            total_earnings -= p[i][1]

    return accepted_requests, total_earnings

n = int(input())  # number of booking requests
k = int(input())  # number of tables
p = []  # list of booking requests (group size, amount spent)

for _ in range(n):
    group_size, amount_spent = map(int, input().split())
    p.append((group_size, amount_spent))

accepted_requests, total_earnings = max_earnings(n, k, p)
print(accepted_requests, total_earnings)  # output

# example output:
# 3 1000
