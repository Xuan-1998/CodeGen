import sys

n = int(input())  # length of the message
s = input()  # message
a = [int(x) for x in input().split()]  # array a

dp = [[0] * (n + 1) for _ in range(n + 1)]
max_length = 0
min_substr = n

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if all(s[k - 1].lower() not in str(ord(ch) - ord('a') + 1) * a[ord(ch.lower()) - 97] for k in range(i, j + 1)):
            dp[i][j] = (dp[i - 1][i - 1] if i > 0 else 1) + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]

for i in range(n, -1, -1):
    if dp[i][n] != 0:
        max_length = max(max_length, j - i + 1)
        min_substr = min(min_substr, j - i + 1)

print((dp[0][n]) % (10**9 + 7))
print(max_length)
print(min_substr)
