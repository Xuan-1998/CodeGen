def find_X_and_Y():
    A = int(input())
    B = int(input())

    # Initialize X, Y, a, and b
    X = 0
    Y = 0
    a = 0
    b = 0

    while True:
        X += 1
        Y = A - X
        if X ^ Y == B:
            break
        if X > A:
            return print(-1)  # No solution exists

    # Print the solution
    print(X, Y)
