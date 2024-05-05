import sys
from functools import lru_cache

# Read input from stdin
A = input().strip()
B = input().strip()

@lru_cache(None)
def LCS(i, j):
    if i == 0 or j == 0:
        return 0
    if A[i-1] == B[j-1]:
        return 1 + LCS(i-1, j-1)
    else:
        return max(LCS(i-1, j), LCS(i, j-1))

max_similarity = 0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        similarity = 4 * LCS(i, j) - (i + j)
        max_similarity = max(max_similarity, similarity)

print(max_similarity)
