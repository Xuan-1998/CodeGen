import sys

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = nums[i]
    
    for j in range(1, k + 1):
        for i in range(j, n):
            if i - j >= 0:
                dp[i][j] = max(dp[i - 1][j - 1] + nums[i], dp[i - 1][j])
            else:
                dp[i][j] = nums[i]
    
    return max(max(row) for row in dp)

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(maxSumSubsequence(nums, k))

if __name__ == "__main__":
    main()
