def canPartition(nums, m):
    n = len(nums)
    dp = [[False] * (m+1) for _ in range(n+1)]

    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(m+1):
            if nums[i-1] <= j:
                dp[i][j+(i)%m] = (dp[i-1][j-nums[i-1]]%m == 0)

    for i in range(n, -1, -1):
        if dp[i][m]%m == 0:
            return 1

    return 0

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(canPartition(nums, m))
