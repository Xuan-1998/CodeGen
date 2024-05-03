import sys

# Input: number of test cases T
T = int(input())

for _ in range(T):
    # Input: number of tickets n
    n = int(input())
    
    # Initialize dp table with zeros
    dp = [[0.0 for _ in range(n+1)] for _ in range(17)]
    
    # Base case: initial state (no distinct numbers, n tickets)
    dp[0][n] = 1
    
    # Process each ticket
    for i in range(2):
        p1, num1, num2 = map(float, input().split())
        for j in range(n-1, -1, -1):
            if num1 not in [num2 for _, num2 in dp[i]]:
                dp[i+1][j] += dp[i][j-1] * (p1 + p2)
            dp[i][j] += dp[i][j-1] * (1-p1-p2)
    
    # Calculate and print the final probability
    sys.stdout.write('%.6f\n' % dp[16][0])
