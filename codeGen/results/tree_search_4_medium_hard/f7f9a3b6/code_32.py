import sys; input = sys.stdin.readline

n = int(input())
s = input().strip()
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(1, min(i // a[ord(s[i - 1]) - 97], i) + 1):
        dp[i][j] = (dp[i - 1][j - 1] * a[ord(s[i - 1]) - 97] + j) % (10 ** 9 + 7)

print(dp[n][1])

max_len = 0
for i in range(2, n + 1):
    for j in range(1, min(i // a[ord(s[i - 1]) - 97], i) + 1):
        if dp[i][j] > max_len:
            max_len = dp[i][j]

print(max_len)

min_substrings = n
for i in range(2, n + 1):
    for j in range(1, min(i // a[ord(s[i - 1]) - 97], i) + 1):
        if dp[i][j] < min_substrings:
            min_substrings = dp[i][j]

print(min_substrings)
