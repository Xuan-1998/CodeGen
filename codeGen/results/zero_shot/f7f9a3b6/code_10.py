mod = 10**9 + 7
n, s = input().split()
a = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

dp[0][0] = 1
for i in range(1, n+1):
    for j in range(min(i, 26), -1, -1):
        if a[ord(s[j-1]) - ord('a')] <= i:
            dp[i][j] = (dp[i-j][0] + dp[i-j][1]) % mod
print(dp[n][0])
max_len = max(j for j in range(n+1) if dp[n][j] != 0)
min_substrs = n - max_len
print(max_len)
print(min_substrs)
