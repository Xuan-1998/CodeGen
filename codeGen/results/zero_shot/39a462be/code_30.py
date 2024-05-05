# Python code for the problem
import sys
from functools import lru_cache

@lru_cache(None)
def LCS_length(X , Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                L[i][j] = 0
            elif j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

def get_similarity(A, B):
    n = len(A)
    m = len(B)

    return (4 * LCS_length(A, B)) - (n + m)

# Read the input from stdin
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

# Calculate and print the result to stdout
print(get_similarity(A, B))
