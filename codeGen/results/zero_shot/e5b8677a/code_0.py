def min_mice_cells(board, n, m):
    min_mice_count = 0

    # Check the cells adjacent to the right edge (excluding the bottom-right cell)
    for i in range(n-1):
        if board[i][m-1] == '1':
            min_mice_count += 1

    # Check the cells adjacent to the bottom edge (excluding the bottom-right cell)
    for j in range(m-1):
        if board[n-1][j] == '1':
            min_mice_count += 1

    # Check the bottom-right cell
    if board[n-2][m-1] == '1' or board[n-1][m-2] == '1':
        min_mice_count += 1

    return min_mice_count

def main():
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().split())
        board = [input().strip() for _ in range(n)]
        result = min_mice_cells(board, n, m)
        print(result)

if __name__ == "__main__":
    main()
