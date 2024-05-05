n = int(input())
m = int(input())
dp = [0] * (2*n + 1)

for i in range(n+1):
    dp[i] = 1

for i in range(n+1, m+n+1):
    for j in range(i):
        if i-j > n:
            dp[i] += sum(dp[max(0, i-k) : k+1]) for k in range(j))[0]
        else:
            dp[i] += sum(dp[k] for k in range(max(0, i-j-1), j+1))

print((dp[m] % (10**8 + 7)))
