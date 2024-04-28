s1 = input()
s2 = input()

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

max_length = 0
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])

print(max_length)
