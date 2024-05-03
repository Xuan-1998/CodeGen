from collections import deque

def zero_out_array():
    n = int(input())
    
    # Initialize dp and dp_inv arrays with False values
    dp = [[False] * (n+1) for _ in range(n+1)]
    dp_inv = [[False] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        # Check if the current element is 0. If so, we can make all elements equal to zero
        if input() == '0':
            dp[i][0] = True
            dp_inv[i][0] = True

    # Fill up the dp and dp_inv arrays
    for i in range(n+1):
        dp[0][i] = True
        dp_inv[n][i] = True

    # Traverse from both ends (start and end)
    for i in range(1, n//2 + 1):
        if input() == '0':
            dp[i][0] = True
            dp_inv[n-i][0] = True

        for j in range(i+1, n//2 + 1):
            if input() == '0' and dp[j-1][1]:
                dp[i][j-i] = True
                dp_inv[n-j][n-i-j+i] = True

    # Print the result based on the value of dp[n][0]
    print("YES" if dp[n][0] else "NO")

zero_out_array()
