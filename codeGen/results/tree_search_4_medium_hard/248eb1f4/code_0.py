def find_winner():
    T = int(input())
    winners = [[0] * (X + 1) for _ in range(X + 1)]

    for i in range(1, X + 1):
        for j in range(i):
            winners[i][j] = ((j + M - 2) % X) + 1

    for i in range(X, 0, -1):
        for j in range(X):
            if i == 1:
                winners[i][j] = (j + M - 1) % X + 1
            else:
                winners[i][j] = winners[i-1][(j+M-2)%X]+1

    result = []
    for i in range(T):
        M, X = map(int, input().split())
        result.append([winners[X][j] for j in range(X)])

    for r in result:
        print(' '.join(map(str, r)))
