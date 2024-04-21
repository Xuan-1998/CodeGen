print('def min_mice_scared_by_elephant(board, n, m):
    dp = [[0] * m for _ in range(n)]

    # Initialize the first row and first column of dp array
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + board[0][i-1]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + board[i-1][0]

    # Fill in the dp array
    for i in range(1, n):
        for j in range(1, m):
            # Calculate the minimum count from the cell above and to the left
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            
            # Check for mice in the adjacent cells to the right and below
            if j < m - 1 and board[i][j] == 1:
                dp[i][j] += 1
            if i < n - 1 and board[i][j] == 1:
                dp[i][j] += 1

    return dp[-1][-1]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    n, m = map(int, input().strip().split())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]
    result = min_mice_scared_by_elephant(board, n, m)
    print(result)')