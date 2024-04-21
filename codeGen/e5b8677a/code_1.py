print('def min_mice_scared(n, m, board):
    dp = [[0] * m for _ in range(n)]
    
    # Check for mice in the first row and first column
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if board[i][j] == '1':
                dp[i][j] = 1
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            if i < n-1 and board[i+1][j] == '1':
                dp[i][j] = 1
            if j < m-1 and board[i][j+1] == '1':
                dp[i][j] = 1
    
    # Traverse the rest of the board
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] += min(dp[i-1][j], dp[i][j-1])

    return dp[n-1][m-1]

# Read number of test cases
T = int(input().strip())

for _ in range(T):
    # Read board size
    n, m = map(int, input().split())
    # Read board
    board = [input().strip() for _ in range(n)]
    # Get the result
    result = min_mice_scared(n, m, board)
    # Print the result
    print(result)')