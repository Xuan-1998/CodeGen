code
n = int(input())
a = [int(x) for x in input().split()]

dp = [0] * (n + 1)
dp_divisible_by_i = [0] * (n + 1)

dp[0] = 1

for i in range(1, n + 1):
    if a[i - 1] % i != 0:
        dp[i] += dp[i - 1]
    else:
        dp_divisible_by_i[i] = dp_divisible_by_i[i - 1]

result = (dp[n] + sum(dp_divisible_by_i)) % (10**9 + 7)
print(result)
