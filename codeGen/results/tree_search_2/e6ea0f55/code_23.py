def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the first row of the DP table
    for j in range(k + 1):
        if j < nums[0]:
            dp[0][j] = nums[0]
        else:
            dp[0][j] = -float('inf')

    for i in range(1, n):
        for j in range(k + 1):
            # If the current element is within k indices of the previous one
            if j < k:
                dp[i][j] = max(dp[i-1][j], dp[i-1][k-j-1] + nums[i])
            else:
                dp[i][j] = dp[i-1][j]

    # Return the maximum sum found in the DP table
    return max(max(row) for row in dp)

def main():
    nums = [int(x) for x in input().split()]
    k = int(input())
    print(maxSumSubsequence(nums, k))

if __name__ == "__main__":
    main()
