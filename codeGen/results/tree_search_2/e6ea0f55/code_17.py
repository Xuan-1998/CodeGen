from sys import stdin

def solve():
    nums = list(map(int, stdin.readline().split()))
    k = int(stdin.readline())
    
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n)]
    
    # Initialize the DP table
    for j in range(k+1):
        dp[0][j] = nums[0]
    
    # Fill up the DP table
    for i in range(1, n):
        for j in range(min(k+1, n-i)):
            dp[i][j] = max(dp[i-1][min(j-1, k)+1] + nums[i], dp[i-1][j] + nums[i])
    
    # Find the maximum sum
    res = 0
    for i in range(1, n):
        res = max(res, dp[i][min(k+1, n-i)])
    
    print(res)

if __name__ == "__main__":
    solve()
