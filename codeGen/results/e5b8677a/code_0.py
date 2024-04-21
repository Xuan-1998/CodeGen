print('def read_input():
    T = int(input())
    test_cases = []
    for _ in range(T):
        n, m = map(int, input().split())
        board = [list(map(int, input().strip())) for _ in range(n)]
        test_cases.append((n, m, board))
    return test_cases

def min_mice_scared(n, m, board):
    # Initialize the dp array with zeros
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # Fill in the first row and first column
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = board[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + board[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + board[i][j]
            else:
                # Check for mice in the current cell and the cells that the elephant has passed through
                mice = board[i][j]
                if board[i-1][j] == 1:  # Check the cell above
                    mice = 1
                if board[i][j-1] == 1:  # Check the cell to the left
                    mice = 1
                # Take the minimum of the two previous cells (above and to the left)
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mice
    
    # The answer will be in the bottom-right corner of the dp array
    return dp[n-1][m-1]

def main():
    test_cases = read_input()
    for n, m, board in test_cases:
        print(min_mice_scared(n, m, board))

if __name__ == "__main__":
    main()')