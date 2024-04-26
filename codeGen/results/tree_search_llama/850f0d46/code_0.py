def chessboard_pattern():
    rows, columns = map(int, input().split())
    pattern = {}

    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                pattern[(i, j)] = "O"  # White
            else:
                pattern[(i, j)] = "X"   # Black

    for row in range(rows):
        for col in range(columns):
            print(pattern.get((row, col), "."), end=" ")
        print()

chessboard_pattern()
