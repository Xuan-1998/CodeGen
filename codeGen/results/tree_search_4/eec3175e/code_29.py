def find_subset(nums, m):
    n = len(nums)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][m]

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(find_subset(nums, m))

if __name__ == "__main__":
    main()
