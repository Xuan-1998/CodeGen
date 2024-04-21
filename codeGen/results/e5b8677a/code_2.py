print('def read_input():
    T = int(input().strip())
    test_cases = []
    for _ in range(T):
        n, m = map(int, input().split())
        board = [list(map(int, input().strip())) for _ in range(n)]
        test_cases.append((n, m, board))
    return test_cases

def min_mice_scared(n, m, board):
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = board[0][0]

    # Fill the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + board[0][j]
        if j < m - 1:
            dp[0][j] += board[0][j+1]

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + board[i][0]
        if i < n - 1:
            dp[i][0] += board[i+1][0]

    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            dp[i][j] += board[i][j]
            if i < n - 1:
                dp[i][j] += board[i+1][j]
            if j < m - 1:
                dp[i][j] += board[i][j+1]

    # The elephant ends at the bottom-right corner
    return dp[n-1][m-1]

def main():
    test_cases = read_input()
    for n, m, board in test_cases:
        result = min_mice_scared(n, m, board)
        print(result)

if __name__ == "__main__":
    main()')