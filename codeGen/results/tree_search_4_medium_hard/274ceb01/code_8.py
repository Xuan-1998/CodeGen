dp = [0] * (n + 1)
total_marks = 0
for i in range(1, n + 1):
    total_marks += i
    if i > 0:
        dp[i] = min(dp[i-1], total_marks - sum(range(1, i+1)))
    else:
        dp[i] = 0

print(min(dp))
