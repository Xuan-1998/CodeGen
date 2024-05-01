n = int(input())  # read the number of elements
a = list(map(int, input().split()))  # read the sequence

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    for j in range(1, i):
        if a[j] == a[i]:
            dp[i][j] = max(dp[j][k] + (i - k) for k in range(j - 1, i)) or 0
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[n][j] for j in range(n)))  # maximum points earned
