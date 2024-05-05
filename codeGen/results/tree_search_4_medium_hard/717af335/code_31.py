from itertools import zip_longest

def solution():
    A, B = map(int, input().split())
    states = [[float('inf')] * (B+1) for _ in range(A+1)]
    states[0][0] = 0

    for a in range(A+1):
        for b in range(B+1):
            if a + b >= a ^ b:
                states[a][b] = min(states[a][b], a)
            else:
                states[a][b] = -1
    X, Y = float('inf'), float('inf')
    for x, y in zip_longest(reversed(range(A+1)), reversed(range(B+1))):
        if states[x][y] != -1 and (X == float('inf') or x < X):
            X, Y = x, y

    print(X, Y) if X != float('inf') else print(-1)

solution()
