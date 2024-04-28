def generate_chessboard(rows, cols):
    chessboard = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if (_ % 2 == 0):  # Even index, add 'O' (white)
                row.append('O')
            else:  # Odd index, add 'X' (black)
                row.append('X')
        chessboard.append(row)

    return chessboard

def main():
    rows, cols = map(int, input().split())
    chessboard = generate_chessboard(rows, cols)

    for row in chessboard:
        print(' '.join(row))

if __name__ == "__main__":
    main()
