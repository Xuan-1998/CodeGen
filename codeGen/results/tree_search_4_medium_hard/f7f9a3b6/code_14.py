import sys; input = lambda: map(int, raw_input().split())

n = next(input)
s = ''.join(input())
a = list(map(int, input()))

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    if s[i-1].isalpha():
        for j in range(i, 0, -1):
            if all(ord(c)-97 <= a[ord(s[k-1])-97] for k in range(j, i, -1)):
                dp[i][j] += dp[i-1][j-1]
    else:
        dp[i][i] = 1

print(sum(dp[n][i] for i in range(n+1))) % (10**9 + 7)
print(max(i for i in range(n+1) if dp[n][i]))
print(min(i for i in range(1, n+1) if dp[n][n-i]))
