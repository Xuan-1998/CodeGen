def distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[set() for _ in range(max_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0].add(0)

    for i in range(n):
        for j in range(max_sum + 1):
            if nums[i] <= j:
                dp[i + 1][j] = set.union(dp[i][j], dp[i][j - nums[i]], {j - nums[i]})
            else:
                dp[i + 1][j] = dp[i][j]

    distinct_sums = set()
    for i in range(max_sum + 1):
        if len(dp[n][i]) > 0:
            distinct_sums.add(i)

    return ' '.join(map(str, sorted(list(distinct_sums))))


# Read input
N = int(input())
nums = list(map(int, input().split()))

print(distinct_sums(nums))
