def is_divisible(sub, k):
    return all(x % k == 0 for x in sub)

n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    for j in range(i):
        if is_divisible(a[j:i+1], j + 1):
            dp[i] += dp[j]

print((dp[n] % (10**9 + 7)))
