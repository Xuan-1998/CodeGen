def count_ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i // 10] + (i % 10 == 1)
    return sum(dp)

n = int(input())
if n > 10**9:
    print("n is too large")
else:
    print(count_ones(n))
