while True:
    A = int(input())
    B = int(input())

    X = 0
    while X <= B:
        Y = A - X
        if X ^ Y == B:
            print(f"{X} {Y}")
            break
        X += 1

    else:
        print("-1")
