mod = 10**9 + 7

def dp_func(i, max_and):
    if i in dp:
        return dp[i]
    and_count = 0
    for j in range(1 << k):  # Loop through all possible k-bit integers
        xor_sum = 0
        and_sum = 0
        for num in range(i+1):
            and_sum |= (j >> (k - 1)) & 1
            xor_sum ^= nums[num]
        if and_sum >= max_and:
            and_count += dp_func(i-1, and_sum) % mod
    dp[i] = and_count % mod
    return and_count

dp = {0: 1}
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(dp_func(n-1, (1 << k) - 1) % mod)
