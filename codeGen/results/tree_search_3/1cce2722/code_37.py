import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * 106 for _ in range(n + 1)]
    
    # Initialize the base case: when i = 0, dp[i][k] should be initialized to k
    for k in range(106):
        dp[0][k] = k
    
    for i in range(1, n + 1):
        for k in range(106):
            if a[i - 1] > k:
                # If ai is not deleted (or deleted along with all elements equal to aj + 1 and aj - 1)
                dp[i][k] = max(dp[i][k], dp[i - 1][k])
            else:
                # If ai is deleted alone
                dp[i][k] = max(dp[i][k], dp[i - 1][a[i - 1] + 1] if a[i - 1] + 1 <= k else -float('inf'), 
                                dp[i - 1][a[i - 1] - 1] if a[i - 1] - 1 >= 0 and a[i - 1] - 1 <= k else -float('inf'))
    
    return max(dp[n])

print(solve())
