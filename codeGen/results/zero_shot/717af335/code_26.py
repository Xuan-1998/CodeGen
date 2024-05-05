import sys

def find_solution(A, B):
    for X in range(A + 1):
        Y = A - X
        if X ^ Y == B:
            return f"{X} {Y}"
    return "-1"

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

print(find_solution(A, B))
