import sys

def count_matrices(N):
    if N % 2 == 0:
        return int((N ** 2) // 8)
    else:
        return int((N ** 2 - 1) // 8 + 1)

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
