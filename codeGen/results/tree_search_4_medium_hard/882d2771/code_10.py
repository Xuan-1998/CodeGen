code_block
t0 = int(input())
l, r = map(int, input().split())

dp = {i: i for i in range(l, r+1)}

for n in range(l, r+1):
    dp[n] = 1 + min(dp[i] for i in range(l, n))

print((t0*dp[l]) + (r-l)*dp[r])
