from collections import defaultdict

def maxSum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the base case: when there are no elements or only one element left
    for i in range(k + 1):
        dp[0][i] = nums[0]
        
    for i in range(1, n):
        for j in range(min(i + 1, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + nums[i]) if i >= k else max(dp[i-1][j], nums[i])

    return max(max(row) for row in dp)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    nums = list(map(int, (input().split())))
    print(maxSum(nums, k))
