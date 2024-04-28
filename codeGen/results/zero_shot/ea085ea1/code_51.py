N = int(input())
str1 = input()
str2 = input()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

max_len = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_len = max(max_len, dp[i][j])

ans = max_len

print(ans)
