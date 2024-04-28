def distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)

    dp = [[set() for _ in range(max_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0].add(0)

    for i in range(1, n + 1):
        for j in range(max_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j].update(dp[i - 1][j - nums[i - 1]] | {x + nums[i - 1] for x in dp[i - 1][j]})
            else:
                dp[i][j].update(dp[i - 1][j])

    return ' '.join(map(str, sorted({x for sublist in dp[n] for x in sublist})))

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    print(distinct_sums(nums))
