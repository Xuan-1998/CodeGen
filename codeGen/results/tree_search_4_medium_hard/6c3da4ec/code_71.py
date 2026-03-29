n = int(input())
s = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if s[j - i:j].count('1') > 0:
            dp[i][j] = max(dp[i-1][k-1] | int(s[k-j:k], 2) for k in range(j))
        else:
            dp[i][j] = int(s[j-i:j], 2)

print(bin(max([dp[0][i] for i in range(n + 1)]))[2:].zfill(n).lstrip('0'))
