def can_sum_subset(nums, m):
    n = len(nums)
    dp = [[False] * m for _ in range(n+1)]

    # Base case: an empty set has a sum of 0 which is divisible by any value
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(m):
            if j % m == 0:
                dp[i][j] = True
            elif dp[i-1][j]:
                dp[i][j] = True
            else:
                for k in range(nums[i-1], m):
                    if (j + k) % m == 0 and dp[i-1][k]:
                        dp[i][j] = True
                        break

    return dp[n][m-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(can_sum_subset(nums, m))
