import sys

# read input from stdin
t, l, r = map(int, input().split())

dp = [0] * (r - l + 1)
for k in range(l, r + 1):
    dp[k-l] = min((k-1)//i + dp[(k-1)%i] for i in range(2, min(k-1, 10000)))

# calculate the result
result = sum(t[i] * (dp[i] if i < r - l else dp[r-l]) for i in range(r-l+1)) - l * dp[r-l]
print(result % (10**9 + 7))
