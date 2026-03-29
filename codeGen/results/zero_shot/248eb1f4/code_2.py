def calculate_winner():
    T = int(input())
    for _ in range(T):
        M, X = map(int, input().split())
        if X == 1:
            print(1)
        elif X <= M:
            print(X - (M - 2) * ((X - 1) // (M - 1)) + 1)
        else:
            print((X - M + 1))

calculate_winner()
