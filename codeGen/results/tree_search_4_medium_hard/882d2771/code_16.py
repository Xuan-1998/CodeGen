import sys

t, l, r = map(int, input().split())

dp = [0] * (r + 1)
for i in range(l, r):
    dp[i] = min(dp[j] for j in range(i))
print(sum(ti*dp[li+di] - li*dp[ri] for ti, li, ri, di in zip(map(int, input().split()), [l]+[l+i for i in range(r-l+1)], [r]+[r+i for i in range(r-l+1)], [0]+[i for i in range(r-l+1)])))
