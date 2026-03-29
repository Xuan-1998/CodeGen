def findXY(A, B):
    X = 0
    while True:
        Y = A - X
        if Y >= 0 and X ^ Y == B:
            return f"{X} {Y}"
        elif Y < 0:
            return "-1"

A = int(input())
B = int(input())

print(findXY(A, B))
