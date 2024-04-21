def mex(col):
    if col == "00":
        return 2
    elif col == "01" or col == "10":
        return 1
    else:  # "11"
        return 0

def solve(n, top, bottom):
    # Initialize the DP array
    dp = [[0, 0] for _ in range(n+1)]
    
    for i in range(1, n+1):
        col = top[i-1] + bottom[i-1]
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][1] + mex(col)

        # If the current column is "00", we must cut here
        if col == "00":
            dp[i][1] = dp[i][0] + mex(col)
    
    return max(dp[n][0], dp[n][1])

# Read the number of test cases
t = int(input().strip())
for _ in range(t):
    # Read the number of columns and the two binary strings
    n = int(input().strip())
    top = input().strip()
    bottom = input().strip()
    # Solve the test case and output the result
    print(solve(n, top, bottom))
