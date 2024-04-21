def min_mice_cells(n, m, board):
    # Initialize the dp array
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the first row and first column of dp
    for i in range(n):
        for j in range(m):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + (1 if board[i][j-1] == '1' else 0)
            elif j == 0 and i > 0:
                dp[i][j] = dp[i-1][j] + (1 if board[i-1][j] == '1' else 0)

    # Calculate the dp values for the rest of the cells
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            if i < n - 1 and board[i+1][j] == '1':
                dp[i][j] += 1
            if j < m - 1 and board[i][j+1] == '1':
                dp[i][j] += 1

    # The answer is the value at the bottom-right corner of the dp array
    return dp[-1][-1]

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    result = min_mice_cells(n, m, board)
    print(result)