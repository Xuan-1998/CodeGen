import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for _ in range(n-1)]

    # Initialize DP table
    dp = [[0] * (10**9 + 1) for _ in range(n+1)]
    
    # Fill DP table using state transition and memoization
    for i in range(2, n+1):
        for j in range(ranges[i-1][0], ranges[i-1][1]+1):
            if p[i] != -1:
                dp[i][j] = 1 + min(dp[p[i]][k] for k in range(j, ranges[p[i]][1]))
            else:
                dp[i][j] = 1
        dp[i][ranges[i-1][0]] = 0
    
    # Return the minimum number of operations needed to adjust the root node's value to its range
    return dp[1][ranges[0][1]]

if __name__ == "__main__":
    for _ in range(int(input())):  # Read T test cases
        print(solve())
