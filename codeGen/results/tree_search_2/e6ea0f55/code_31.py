def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = {0: 0}

    for i in range(1, n):
        dp[i] = max(dp.get(max(0, i-k), 0) + nums[i], dp[max(0, i-k)][min(k, i)])

    return max(dp.values())

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    print(max_sum_subsequence(nums, k))
