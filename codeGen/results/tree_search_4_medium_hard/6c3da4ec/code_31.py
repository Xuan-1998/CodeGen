import sys

n = int(input())  # read n from stdin
s = input()  # read binary string s of length n from stdin

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[i][j] = max((dp[i-1][k] | int(s[k])) | dp[k+1][j] for k in range(i, j))

print(bin(dp[n][n]).replace("0b", ""))  # print the maximum bitwise OR value as a binary string
