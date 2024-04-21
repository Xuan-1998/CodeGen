print('def min_mice_scared_by_path(board, n, m):
    # Initialize the dp array with zeros
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the first row and first column
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + board[0][i-1]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + board[i-1][0]
    
    # Fill in the rest of the dp array
    for i in range(1, n):
        for j in range(1, m):
            from_top = dp[i-1][j] + board[i-1][j]
            from_left = dp[i][j-1] + board[i][j-1]
            dp[i][j] = min(from_top, from_left)
    
    # Add the mice that might scare the elephant in the last move
    dp[n-1][m-1] += board[n-1][m-1] or board[n-1][m-2] or board[n-2][m-1]
    
    return dp[n-1][m-1]

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    n, m = map(int, input().strip().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    result = min_mice_scared_by_path(board, n, m)
    print(result)')