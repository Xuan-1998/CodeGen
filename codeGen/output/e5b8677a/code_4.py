print('def read_ints():
    return list(map(int, input().split()))

def min_mice_scare(mice_board, n, m):
    dp = [[0] * m for _ in range(n)]

    # Check for mice adjacent to the start cell
    if mice_board[0][1] == '1':
        dp[0][0] += 1
    if mice_board[1][0] == '1':
        dp[0][0] += 1

    # Fill the first row and first column of dp
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + (mice_board[0][i] == '1' and mice_board[0][i-1] == '0')
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + (mice_board[i][0] == '1' and mice_board[i-1][0] == '0')

    # Fill the rest of the dp array
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            if mice_board[i][j] == '1':
                dp[i][j] += 1

    # Add mice that are adjacent to the final cell but not counted
    if mice_board[n-1][m-2] == '1' and dp[n-1][m-1] == dp[n-1][m-2]:
        dp[n-1][m-1] += 1
    if mice_board[n-2][m-1] == '1' and dp[n-1][m-1] == dp[n-2][m-1]:
        dp[n-1][m-1] += 1

    return dp[n-1][m-1]

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n, m = read_ints()
    mice_board = [input().strip() for _ in range(n)]
    result = min_mice_scare(mice_board, n, m)
    print(result)')