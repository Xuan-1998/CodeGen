code
dp = [0] * (r + 1)
for i in range(2, r + 1):
    if i == 1:
        dp[i] = i - 1
    else:
        dp[i] = 1 + min(dp[i-1], dp[i-i])
t = t0 * f(l) + t1 * f(l+1) + ... + tr * f(r) - l * f(r)
print((t % (109 + 7)).astype(int))
