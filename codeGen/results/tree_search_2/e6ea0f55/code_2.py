def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = nums[i]
        for j in range(1, min(i, k) + 1):
            if i - j >= 0:
                dp[i][j] = max(dp[i][j], dp[i-j-1][j-1] + nums[i])
            else:
                dp[i][j] = nums[i]

    return max(max(row) for row in dp)

def main():
    k, *nums = [int(x) for x in input().split()]
    print(max_sum_subsequence(nums, k))

if __name__ == "__main__":
    main()
