def findX(A, B):
    if A < B:
        return -1

    for X in range((A >> 1) + 1):
        Y = A - X
        if X ^ Y == B:
            return X

    return -1

def solve():
    A = int(input())
    B = int(input())
    result = findX(A, B)
    print(result)

solve()
