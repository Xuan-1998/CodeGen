def min_mice_scared(n, m, board):
    # Initialize the dp array with zeros
    dp = [[0] * m for _ in range(n)]

    # Set the first cell to 0 as it does not scare the elephant
    dp[0][0] = 0

    # Fill the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + board[0][j - 1]

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + board[i - 1][0]

    # Fill the rest of the cells
    for i in range(1, n):
        for j in range(1, m):
            # Calculate the number of mice that scare the elephant from the left and above
            mice_scared = board[i - 1][j] + board[i][j - 1]
            # Choose the minimum path to reach this cell
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + mice_scared

    # Return the number of mice that scare the elephant at the bottom-right corner
    return dp[-1][-1]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    # Read the size of the board
    n, m = map(int, input().strip().split())
    # Read the board configuration
    board = [list(map(int, list(input().strip()))) for _ in range(n)]
    # Calculate and print the result
    print(min_mice_scared(n, m, board))
