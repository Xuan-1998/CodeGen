from collections import defaultdict

N = int(input())
str1 = input().strip()
str2 = input().strip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
max_length = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])

ans = defaultdict(int)
for i in range(len(str1) - max_length + 1):
    for j in range(len(str2) - max_length + 1):
        if str1[i:i + max_length] == str2[j:j + max_length]:
            ans[len(str1[i:i + max_length])] += 1

print(sum(ans.values()))
