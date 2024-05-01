from collections import defaultdict

def distinct_sum_sets(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[0] * (max_sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(max_sum + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - nums[i - 1]] if j - nums[i - 1] >= 0 else 0)

    sums = set()
    for i in range(max_sum + 1):
        if dp[n][i]:
            sums.add(i)
    return ' '.join(map(str, sorted(list(sums))))


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(distinct_sum_sets(nums))
