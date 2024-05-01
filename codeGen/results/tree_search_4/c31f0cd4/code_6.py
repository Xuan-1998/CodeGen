def distinct_sum_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[0] * (max_sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for j in range(1, n + 1):
        for k in range(max_sum + 1):
            if nums[j - 1] <= k:
                dp[j][k] = dp[j - 1][k] + dp[j - 1][k - nums[j - 1]]
            else:
                dp[j][k] = dp[j - 1][k]

    distinct_sums = set()
    for j in range(1, n + 1):
        for k in range(max_sum // j + 1):
            if max_sum >= j * k and dp[n][max_sum - j * k]:
                distinct_sums.add(j * k)

    return sorted(list(distinct_sums))

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    print(*distinct_sum_sums(nums), sep=' ')
