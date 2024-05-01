def find_distinct_sums(nums):
    N = len(nums)
    total_sum = sum(nums)
    dp = [[0] * (total_sum + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(1, total_sum + 1):
            if j <= nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    distinct_sums = []
    for i in range(1, total_sum + 1):
        if dp[N][i] > 0:
            distinct_sums.append(i)

    return ' '.join(map(str, sorted(distinct_sums)))


N = int(input())
nums = list(map(int, input().split()))
print(find_distinct_sums(nums))
