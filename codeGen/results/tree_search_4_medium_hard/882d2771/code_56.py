import sys

def f(n):
    if n == 2:
        return 1
    elif n % 2:
        return dp[n-1] + 1
    else:
        return dp[n//2] + (n//2) - n

t, l, r = map(int, input().split())
dp = {i: i for i in range(2, 5*10**6+1)}

for i in range(l, r+1):
    if i % 2:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i//2] + (i//2) - i

print(sum(t*i for i in range(l, r+1)) % (10**9 + 7))
