def ways_to_form_sum(m, N, arr):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in arr:
            if num <= i:
                dp[i] += dp[i - num]
                dp[i] %= MOD

    return dp[N]

m = int(input())
N = int(input())
arr = list(map(int, input().split()))
print(ways_to_form_sum(m, N, arr))
