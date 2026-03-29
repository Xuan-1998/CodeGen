dp = [0] * (n + 1)
for i in range(10):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = 0

ones_in_digits = 2  # ones in digits from 2 to 9
for i in range(10, n+1):
    if i % 10 == 1:
        dp[i] += dp[i // 10]
    elif i % 10 >= 2:
        dp[i] += ones_in_digits

total_count = sum(dp[:n+1])
print(total_count)
