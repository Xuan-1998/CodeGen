from collections import defaultdict

def min_marks_below_water(n, marks):
    dp = [defaultdict(int) for _ in range(n+1)]
    
    # Initialize base case
    for k in range(n):
        dp[0][k] = k * (k + 1) // 2
    
    for i in range(1, n+1):
        for k in range(n-i):
            min_sum = float('inf')
            for j in range(i):
                min_sum = min(min_sum, dp[j][k] + (n - j - 1) - (i - 1 - j))
            dp[i-1][k] = min_sum
    
    return dp[n-1].values()[-1]

# Read input
n = int(input())
marks = list(map(int, input().split()))

print(min_marks_below_water(n, marks))
