def count_ways(m, N):
    dp = {0: 1}
    for num in nums:
        new_dp = {}
        for j in range(N + 1):
            if j >= num:
                new_dp[j] = (new_dp.get(j, 0) or 0) + dp.get(j - num, 0)
            else:
                new_dp[j] = dp.get(j, 0)
        dp = new_dp
    return dp.get(N, 0) % (10**9 + 7)

m, N = map(int, input().split())
nums = list(map(int, input().split()))
print(count_ways(m, N))
