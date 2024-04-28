N = int(input())
str1 = input()
str2 = input()

dp = [[0] * (N + 1) for _ in range(N + 1)]
max_length = 0
count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                count = 1
        elif i == j and str1[i - 1] == str2[j - 1]:
            dp[i][j] = 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                count = 1
        else:
            dp[i][j] = 0

print(count)
