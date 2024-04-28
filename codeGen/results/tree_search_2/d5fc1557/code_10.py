def longest_subarray(nums):
    n = len(nums)
    dp = {0: 1}
    res = 0

    for i in range(n):
        if nums[i] == 1:
            new_key = max(dp.keys(), default=0) + 1
            while new_key in dp and dp[new_key] < i - dp[max(dp.keys())]:
                del dp[dp.pop(max(dp))]
            dp[new_key] = i
        res = max(res, dp.get(i, 0))

    return n - 1 - res

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(longest_subarray(nums))
