import sys

def max_grade(n, t):
    dp = [[False] * (t + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for j in range(t + 1):
        dp[0][j] = True
    
    # Fill up DP table
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if i < 2:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = or(dp[i-1][j], dp[int(i/2)][j-1])
    
    # Return maximum possible grade
    for j in range(t, -1, -1):
        if dp[n][j]:
            return n
    
    return 0

def or(a, b):
    return a or b

if __name__ == "__main__":
    n = int(input())
    t = int(input())
    print(max_grade(n, t))
