import sys

t, l, r = map(int, input().split())

def f(n):
    # Calculate the minimal total number of pairwise comparisons needed
    # for n girls in a beauty contest
    pass  # TO DO: implement the function f(n)

dp = [0] * (r + 1)
for i in range(2, r + 1):
    dp[i] = dp[i - 1] + 1  # TO DO: implement the dynamic programming formula

result = 0
for i in range(t):
    if l <= r:
        result += dp[r]
    else:
        pass  # TO DO: handle the case when l > r

print(result % (10**9 + 7))
